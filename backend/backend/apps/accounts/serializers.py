from backend.apps.accounts.models import User
from rest_framework import serializers
from backend.apps.snippets.models import Snippet


class UserSerializer(serializers.ModelSerializer):
    """
    因为'snippets' 在用户模型中是一个反向关联关系。在使用 ModelSerializer 类时它默认不会被包含，所以我们需要为它添加一个显式字段。
    """
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')