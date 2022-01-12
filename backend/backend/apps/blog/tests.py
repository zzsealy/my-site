from django.test import TestCase
from django.test import Client
from backend.apps.accounts.models import User
from rest_framework.authtoken.models import Token
# Create your tests here.


class test_view(TestCase):

    def setUp(self) -> None:
        u = User(username='test')
        u.set_password('test')
        u.save()
        self.user = u

        self.c = Client()

    def test_func(self):
        token = Token.objects.create(user=self.user)
        token.save()
        auth_headers = {
            'HTTP_AUTHORIZATION': token.key,
        }
        response = self.c.post('/categories', {"cate": "test"}, **auth_headers)
        # print("response.status_code:", response.status_code)
        self.assertEqual(response.status_code, 200)

        response = self.c.get('/categories', **auth_headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], 'test')

        # 修改名字
        put_del_url = '/category/' + str(response.data[0]['id'])
        response = self.c.put(put_del_url, data={
                              "cate_name": "change_test"}, content_type="application/json", **auth_headers)
        self.assertEqual(response.status_code, 200)

        response = self.c.get('/categories', **auth_headers)
        self.assertEqual(response.data[0]['name'], 'change_test')

        response = self.c.delete(put_del_url, **auth_headers)
        self.assertEqual(response.status_code, 200)

        response = self.c.get('/categories', **auth_headers)
        self.assertEqual(len(response.data), 0)
