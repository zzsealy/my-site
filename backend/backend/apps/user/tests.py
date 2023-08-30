from django.test import TestCase, Client
from user.user_dal import user_dal

class UserTestCase(TestCase):

    def setUp(self):
        # 创建用户
        create_info = {
            'email': '123456@qq.com',
            'password': '123456'
        }
        user_dal.create_one_obj(create_info=create_info)

    def test_login(self):
        c = Client()
        response = c.post('/users/login', {'email': '123456@qq.com', 'password': '123456'})
        response_data = response.json()
        self.assertEqual(response_data.get('status_code'), 200)
    
    def test_error_password(self):
        c = Client()
        url = '/users/login'
        data = {'email': '123456@qq.com', 'password': '12345'}
        response_data = c.post(url, data=data).json()
        self.assertEqual(response_data.get('status_code'), 4003)

    def test_register_user(self):
        pass