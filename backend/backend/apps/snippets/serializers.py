# 序列化器例子
from asyncore import read
from gettext import install
from importlib_metadata import requires
from rest_framework import serializers
from backend.apps.snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from rest_framework import permissions

"""
序列化： serializer = SnippetSerializer(snippet)
        serializer.data
序列化转化成JSON： content = JSONRenderer().render(serializer.data)
反序列化：import io    
        stream = io.BytesIO(content)
        data = JSONParser().parse(stream)
python原生数据类型恢复成正常的对象实例：  serializer = SnippetSerializer(data=data)
                                    serializer.is_valid()
                                    # True
                                    serializer.validated_data
                                    # OrderedDict([('title', ''), ('code', 'print "hello, world"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
                                    serializer.save()
                                    # <Snippet: Snippet object>
我们也可以序列化查询结果集（querysets）而不是模型实例。我们只需要为serializer添加一个many=True标志。
serializer = SnippetSerializer(Snippet.objects.all(), many=True)
serializer.data
"""


# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

#     def create(self, validated_data):
#         """
#         根据提供的验证过的数据创建并且返回一个新的 ‘Snipptet’ 实例。
#         """
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         根据提供的验证过的数据更新和返回一个已经存在的'Snippet'实例。
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance


# 下面是 modelSerialize 类似 modelform
"""
序列一个非常棒的属性就是可以通过打印序列化器类实例的结构(representation)查看它的所有字段.
from snippets.serializers import SnippetSerializer
serializer = SnippetSerializer()
print(repr(serializer))

重要的是要记住，ModelSerializer类并不会做任何特别神奇的事情，它们只是创建序列化器类的快捷方式：

一组自动确定的字段。
默认简单实现的create()和update()方法。
"""


# class SnippetSerializer(serializers.ModelSerializer):
    
#     owner = serializers.ReadOnlyField(source='owner.username')
#     """
#     注意：确保你还将'owner',添加到内部Meta类的字段列表中。

#     这个字段非常有趣。source参数控制哪个属性用于填充字段，并且可以指向序列化实例上的任何属性。它也可以采用如上所示点加下划线的方式，
#     在这种情况下，它将以与Django模板语言一起使用的相似方式遍历给定的属性。

#     我们添加的字段是无类型的ReadOnlyField类，区别于其他类型的字段（如CharField，BooleanField等）。无类型的ReadOnlyField始终是只读的，只能用于序列化表示，
#     不能用于在反序列化时更新模型实例。我们也可以在这里使用CharField(read_only=True)
#     """
#     class Meta:
#         model = Snippet
#         fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')
