import django_filters

from backend.utils.constants.todo_constant import TagConstant, StatusConstant
from todo.models import TodoList, Todo


class TodoListFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(method='id_filter')
    tag = django_filters.CharFilter(method='tag_filter')
    status = django_filters.CharFilter(method='status_filter')

    class Meta:
        model = TodoList
        fields = ['id', 'tag', 'status']
    
    def id_filter(self, queryset, field_name, value):
        return queryset.filter(id=value)
    
    def tag_filter(self, queryset, field_name, tag):
        tag = TagConstant[tag.upper()].value
        return queryset.filter(tag=tag).order_by('-create_datetime')
    
    def status_filter(self, queryset, field_name, status):
        status = StatusConstant[status.upper()].value
        return queryset.filter(is_close=status).order_by('-create_datetime')

class TodoFilter(django_filters.FilterSet):
    list_id = django_filters.CharFilter(method='list_id_filter')

    class Meta:
        model = Todo
        fields = ['list_id']
    
    def list_id_filter(self, queryset, field_name, value):
        return queryset.filter(list_id=value)