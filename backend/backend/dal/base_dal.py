from django.db import connection
from django.forms.models import model_to_dict
from itertools import chain
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


class BaseDal(object):

    def __init__(self, model):

        self.model = model

    def create_one_obj(self, create_info, db_select=None, **kwargs):
        """
        创建数据
        :param create_info:
        :return: dict
        """
        create_info = create_info if type(create_info) == dict else dict()
        if not create_info:
            return None
            # 创建对象
        try:
            k_obj = self.model.objects.db_manager(db_select).model(**create_info)
            # force_insert 只能创建
            k_obj.save(force_insert=True)
        except Exception as e:
            print(e)
            k_obj = None
        if k_obj:
            k_obj = model_to_dict(k_obj)
        return k_obj

    def bluk_create(self, create_infos):
        """
        批量创建数据
        :param create_infos: list tuple
        :return: list
        """
        create_infos = create_infos if isinstance(create_infos, (tuple, list, set)) else tuple()
        if not create_infos:
            return None
        models = [self.model(**create_info) for create_info in create_infos]
        try:
            objs = self.model.objects.bulk_create(models)
        except Exception as e:
            print(e)
            objs = None
        if objs:
            objs = [model_to_dict(i) for i in objs]
        return objs

    def get_by_id(self, o_id, db_select=None):
        """
        base dal 根据id获得数据
        :param o_id: id值进查询
        :param db_select: 为实现读写数据库分离预留
        :return:
        """
        try:
            obj = self.model.objects.get(pk=o_id)
        except Exception as e:
            obj = None
        if obj:
            obj = model_to_dict(obj)
        return obj

    def update_by_id(self, o_id, update_info=None, db_select=None, **kwargs):
        """
        base dal 根据id更新信息
        :param o_id: 数据的id   限制id为主键id
        :param db_select: 为实现读写数据库分离预留
        :param update_info: 更新的数据
        :return: 返回的是影响的行数或者None
        """
        update_info = update_info if type(update_info) == dict else dict()
        try:
            obj = self.model.objects.filter(pk=o_id).update(**update_info)
        except Exception as e:
            print(e)
            obj = None
        return obj

    def update_by_filters(self, filters=None, excludes=None, update_info=None, db_select=None, **kwargs):
        """
        base dal 根据查询条件更新数据的信息
        :param filters: 获取符合条件的信息 dict
        :param exclude: 获取符合条件之外的信息 dict
        :param db_select: 为实现读写数据库分离预留
        :param update_info: 更新数据的更新信息 k=v
        :return:
        """
        filters = filters if type(filters) == dict else dict()

        excludes = excludes if type(excludes) == dict else dict()
        if not update_info:
            return None
        if not filters:
            return None

        update_info = update_info if type(update_info) == dict else dict()
        try:
            obj = self.model.objects.filter(**filters).exclude(**excludes).update(**update_info)
        except Exception as e:
            print(e)
            obj = None
        return obj

    def get_model_field_name(self):
        """
        获取模型字段名字
        :return:
        """
        opts = self.model._meta
        values = []
        for f in chain(opts.concrete_fields, opts.private_fields, opts.many_to_many):
            if not getattr(f, 'editable', False):
                continue
            if f.name in values:
                values.append(f.name)
        return values

    def get_info_filters(self, filters=None, excludes=None, order_by=('-pk',), db_select=None, **kwargs):
        """
        base dal 查询多条数据　当条件为空的时候查询全部信息
        :param filters: 返回符合条件的数据 dict
        :param db_select: 为实现读写数据库分离预留
        :param excludes: 返回符合条件之外的数据 dict
        :param order_by: 排序方式　数据类型为元祖 tuple
        :return:
        """
        filters = filters if type(filters) == dict else dict()

        excludes = excludes if type(excludes) == dict else dict()
        values = kwargs.get('values', [])
        if not values:
            values = self.get_model_field_name()
            kwargs['values'] = values
        try:
            select_related = kwargs.pop('select_related')
        except KeyError as e:
            select_related = (None,)

        try:
            k_object_list = self.model.objects.db_manager(db_select).filter(**filters).exclude(**excludes).order_by(
                *order_by).select_related(*select_related).values(*values)
        except Exception as e:
            print(e)
            k_object_list = None
        return k_object_list

    def get_one_by_condition(self, condition, db_select=None, **kwargs):
        """获取一条信息"""
        try:
            obj = self.model.objects.get(**condition)
            dict_info = model_to_dict(obj)
        except ObjectDoesNotExist as e:
            print(e)
            # logging_utils(e)
            dict_info = None
        except MultipleObjectsReturned as e:
            print(e)
            # logging_utils(e)
            dict_info = None

        return dict_info

    def execute_raw_sql(self, sql_text):
        """执行sql"""
        with connection.cursor() as cursor:
            cursor.execute(sql_text)
            row = [dict(zip([desc[0] for desc in cursor.description], row)) for row in cursor.fetchall()]
        return row

    def execute_prevent_injection_raw_sql(self, sql_text, sql_param):
        """
        执行防注入sql
        :param sql_text: select * from `order` where order_id = %(order_id)s
        :param sql_param: dict 迭代器   {'order_id': "ET123"}
        :return:
        """
        if not isinstance(sql_param, (dict)):
            return None

        with connection.cursor() as cursor:
            cursor.execute(sql_text, sql_param)
            row = [dict(zip([desc[0] for desc in cursor.description], row)) for row in cursor.fetchall()]
        return row

    def get_filter_and_fuzzy_queries_list(self, filters=None, q_objs=None, e_q_objs=None, excludes=None, order_by=None, db_select=None, **kwargs):
        """
        条件查询，根据filters（字典）删选数据，然后根据q_objs（Q对象）模糊查询，order_by排序条件，默认主键
        :param filters:
        :param q_objs: 元组类型
        :param e_q_objs: excludes 中的 args 元组类型
        :param order_by:
        :param db_select:
        :param kwargs:
        :return:
        """
        filters = filters if isinstance(filters, dict) else dict()
        excludes = excludes if isinstance(excludes, dict) else dict()
        q_objs = tuple(q_objs) if isinstance(q_objs, (tuple, list, set)) else tuple()
        e_q_objs = tuple(e_q_objs) if isinstance(e_q_objs, (tuple, list, set)) else tuple()
        order_by = tuple(order_by) if isinstance(order_by, (tuple, list, set)) else tuple()
        if not order_by:
            order_by = ('-pk',)
        try:
            obj_list = self.model.objects.filter(*q_objs, **filters).exclude(*e_q_objs, **excludes).order_by(*order_by)
        except Exception as e:
            print(e)
            obj_list = None
        if obj_list:
            obj_list = [model_to_dict(i) for i in obj_list]
        return obj_list

    def delete_mul_obj(self, filters=None, excludes=None, db_select=None, **kwargs):
        """
        xiaofei wang
        :param filters:
        :param excludes:
        :param db_select:
        :param kwargs:
        :return:
        """
        filters = filters if type(filters) == dict else dict()

        excludes = excludes if type(excludes) == dict else dict()
        if not filters:
            return None
        try:
            result = self.model.objects.filter(**filters).exclude(**excludes).delete()
        except Exception as e:
            print(e)
            result = None
        return result