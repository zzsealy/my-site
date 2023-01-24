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


class TodoList(models.Model):
    id = models.IntegerField(db_index=True, primary_key=True)
    user_id = models.IntegerField() # 用户id
    all_finish = models.IntegerField(default=0) # 0未全部完成， 1全部完成
    create_datetime = models.DateTimeField()
    can_change = models.IntegerField(default=0) # 0不可以修改， 可以修改
    finish_rate = models.CharField(default='0/0', max_length=100)


    @property
    def child_todo(self):
        return_list = []
        for todo in Todo.objects.filter(list_id=self.id):
            return_list.append(model_to_dict(todo))
        return return_list
