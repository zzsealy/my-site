import random
from faker import Faker
from accounts.models import User
from blog.models import Post, Category

class FakeData():

    def __init__(self) -> None:
        self.cate_name_list = ['生活', '编程', '学习', '故事']
        self.fake = Faker('zh_CN')

        self.cates = None
    
  


    def fake_cate(self):
        for cate_name in self.cate_name_list:
            Category.objects.create(name=cate_name)
        self.cates = list(Category.objects.all())
    
    def create_post(self):
        for i in range(100):
            post_length = random.randint(1000, 5000)
            body = self.fake.text(post_length)
            cate = random.choice(self.cates)
            owner = User.objects.all()[0]
            create_data = {
                'title': self.fake.sentence(),
                'subhead': body[:50],
                'body': body,
                'cate': cate,
                'owner': owner
            }
            Post.objects.create(**create_data)

    def create(self):
        # self.del_data()
        self.fake_cate()
        self.create_post()


if __name__ == '__main__':
    fake_data = FakeData()
    fake_data.create()