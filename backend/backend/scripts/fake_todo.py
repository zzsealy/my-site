from datetime import datetime
from todo.models import Todo, TodoList

def run():
    try:
        TodoList.objects.all().delete()
        Todo.objects.all().delete()
        TodoList.objects.create(id=1, user_id=1, all_finish=0, create_datetime=datetime.now(), can_change=1, finish_rate='2/3')
        Todo.objects.create(id=1, is_finish=0, finish_time=datetime.now(), body='学习', list_id=1, create_datetime=datetime.now())
        Todo.objects.create(id=2, is_finish=1, finish_time=datetime.now(), body='打球', list_id=1, create_datetime=datetime.now())
        Todo.objects.create(id=3, is_finish=1, finish_time=datetime.now(), body='俯卧撑', list_id=1, create_datetime=datetime.now())

        TodoList.objects.create(id=2, user_id=1, all_finish=1, create_datetime=datetime(2023, 1, 10, 13, 22), can_change=0, finish_rate='3/3')
        Todo.objects.create(id=4, is_finish=1, finish_time=datetime.now(), body='学习1', list_id=2, create_datetime=datetime(2023, 1, 10, 13, 22))
        Todo.objects.create(id=5, is_finish=1, finish_time=datetime.now(), body='打球1', list_id=2, create_datetime=datetime(2023, 1, 10, 13, 22))
        Todo.objects.create(id=6, is_finish=1, finish_time=datetime.now(), body='俯卧撑1', list_id=2, create_datetime=datetime(2023, 1, 10, 13, 22))

        TodoList.objects.create(id=3, user_id=1, all_finish=0, create_datetime=datetime(2022, 12, 26, 7, 0, 0), can_change=0, finish_rate='0/3')
        Todo.objects.create(id=7, is_finish=0, finish_time=datetime.now(), body='学习2', list_id=3, create_datetime=datetime(2022, 12, 26, 7, 0, 0))
        Todo.objects.create(id=8, is_finish=0, finish_time=datetime.now(), body='打球2', list_id=3, create_datetime=datetime(2022, 12, 26, 7, 0, 0))
        Todo.objects.create(id=9, is_finish=0, finish_time=datetime.now(), body='俯卧撑2', list_id=3, create_datetime=datetime(2022, 12, 26, 7, 0, 0))


        TodoList.objects.create(id=4, user_id=1, all_finish=0, create_datetime=datetime(2022, 12, 19, 9, 0, 0), can_change=0, finish_rate='1/3')
        Todo.objects.create(id=10, is_finish=0, finish_time=datetime.now(), body='学习3', list_id=4, create_datetime=datetime(2022, 12, 19, 9, 0, 0))
        Todo.objects.create(id=11, is_finish=0, finish_time=datetime.now(), body='打球3', list_id=4, create_datetime=datetime(2022, 12, 19, 9, 0, 0))
        Todo.objects.create(id=12, is_finish=1, finish_time=datetime.now(), body='俯卧撑3', list_id=4, create_datetime=datetime(2022, 12, 19, 9, 0, 0))
    except Exception as e:
        print('创建发生错误:', e)

if __name__ =='__main__':
    run()