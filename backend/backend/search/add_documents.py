from elasticsearch_dsl import Index, connections
from elasticsearch import Elasticsearch

# from apps.blog.models import Post
from backend.apps.blog.models import Post


posts = Post.objects.all()
es = Elasticsearch()

def create_document():
    es.indices.delete(index='post') # 把旧的删除
    try:
        connect = connections.create_connection(hosts=['localhost'], timeout=20)
        i = Index('post', using=connect)
    except Exception as e:
        print(e)
    
    for post in posts:
        document_body_dict = dict()
        document_body_dict['title'] = post.title
        document_body_dict['subhead'] = post.subhead
        document_body_dict['body'] = post.body
        document_body_dict['cate'] = post.cate.name
        document_body_dict['created'] = str(post.created).replace('T', ' ').split('.')[0]
        es.index(index = 'post', body=document_body_dict, id=post.id)


create_document()
