from elasticsearch_dsl import Index, Document, Date, Text, Boolean, Float, Integer, Keyword, Long, connections, Object, Short
from django.conf import settings

try:
    connect = connections.create_connection(hosts=['localhost'], timeout=20)
    i = Index('post', using=connect)
except Exception as e:
    print(e)

@i.document
class PostDoc(Document):
    title = Keyword()
    subtitle = Text()
    content = Text()
    cate = Keyword()
    created = Date()

def init_doc():
    i.create()


init_doc()

