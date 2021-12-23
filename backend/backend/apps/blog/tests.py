from django.test import TestCase
from django.test import Client
# Create your tests here.


class test_view(TestCase):

    def setUp(self) -> None:
        self.c = Client()
    
    def test_func(self):
        response = self.c.post('/categories', {"cate": "test"})
        # print("response.status_code:", response.status_code)
        self.assertEqual(response.status_code, 200)

        response = self.c.get('/categories')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], 'test')

        # 修改名字
        put_del_url = '/category/' + str(response.data[0]['id'])
        response = self.c.put(put_del_url, data={"cate_name": "change_test"}, content_type="application/json")
        self.assertEqual(response.status_code, 200)


        response = self.c.get('/categories')
        self.assertEqual(response.data[0]['name'], 'change_test')

        response = self.c.delete(put_del_url)
        self.assertEqual(response.status_code, 200)


        response = self.c.get('/categories')
        self.assertEqual(len(response.data), 0)


