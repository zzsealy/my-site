from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from fastapi import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from backend.apps.snippets.models import Snippet
from backend.apps.snippets.serializers import SnippetSerializer
# Create your views here.


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content in JSON
    """ 
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def snippet_list(request):
    """
    列出所有的code snippet， 或者创建一个新的snippet
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JSONResponse(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser.parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONRenderer(serializer.errors, status=100)


@csrf_exempt
def snippet_detail(request, pk):
    """
    获取，更新， 或者删除一个code snippet
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser.parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

