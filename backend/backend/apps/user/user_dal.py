import hashlib
from backend.dal.base_dal import BaseDal
from .models import User
from django.conf import settings

class UserDal(BaseDal):
    SECRET_KEY = settings.SECRET_KEY

    def __init__(self):
        super().__init__(model=User)

    @staticmethod 
    def generate_password(password: str) -> str:
        return hashlib.sha1(password.encode('utf-8') + b'self.SECRET_KEY').hexdigest()

    def create_one_obj(self, create_info, db_select=None, **kwargs):
        password = create_info.get('password')
        create_info['password'] = self.generate_password(password=password)
        return super().create_one_obj(create_info, db_select, **kwargs) 
    
    def check_password(self, username, password):
        user = self.get_one_by_condition(condition={'username': username}) 
        if user.get('password') == self.generate_password(password):
            return True
        return False



user_dal = UserDal()