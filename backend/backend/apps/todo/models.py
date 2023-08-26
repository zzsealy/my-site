from datetime import datetime
from django.db import models
from django.forms import model_to_dict

# Create your models here.


class Todo(models.Model):
    id = models.IntegerField(db_index=True, primary_key=True)
    create_datetime = models.DateTimeField()
    is_finish = models.IntegerField(default=0) # 0未完成，1完成
    finish_time = models.DateTimeField(blank=True)
    body = models.TextField() # 待办事项的具体内容
    list_id = models.IntegerField(blank=True)  # 属于那个待办事项的列表


class TodoList(models.Model):  # 与todo是一对多关系
    id = models.IntegerField(db_index=True, primary_key=True)
    user_id = models.IntegerField() # 用户id
    title = models.CharField(default='未填写标题', max_length=200)
    create_datetime = models.DateTimeField(auto_now=True, help_text='创建时间')
    close_datetime = models.DateField(auto_now=True, help_text='关闭时间 根据is_close字段来判断是否关闭')
    expect_finish_date = models.DateTimeField(auto_now=True, help_text='预计完成时间')
    is_close = models.SmallIntegerField(default=0, help_text='0: 未关闭 1: 关闭')
    finish_rate = models.CharField(default='0/0', max_length=100)
    tag = models.IntegerField(default=0, help_text='0:周目标 1:月目标 2:短期目标 3:长期目标')

    @property
    def child_todo(self):
        return_list = []
        for todo in Todo.objects.filter(list_id=self.id):
            return_list.append(model_to_dict(todo))
        return return_list
