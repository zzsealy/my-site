import json
import datetime

from django.conf import settings
from django.utils.timezone import localtime
from django.utils.deprecation import MiddlewareMixin
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.http import JsonResponse

class Middleware(MiddlewareMixin):

    def process_request(self, request, **kwargs):
        # login_verify_status = self.verify_login_validity(request)
        # request.user = login_verify_status['user']  # 成功就返回用户的user 否则返回用户的
        # if login_verify_status['result'] is False:
        #     return JsonResponse({'status_code': 401})
        return Response
        # return JsonResponse(data={"susscess":0, "message":"记录事件开始到数据库出错"}, content_type='application/json', status=401)

    
    def verify_login_validity(self, request):
        token_key = request.META.get('HTTP_AUTHORIZATION', None)
        url_info = settings.URL_VERIFICATION_LIST.get(request.path)
        status = self.verify_bearer_token(token_key=token_key)
        if url_info and request.method in url_info:
            # 如果url在忽略token验证的路由和方法里，就不进行token验证
            status['result'] = None 
        
        return status
    

    def verify_bearer_token(self, token_key):
        token = Token.objects.filter(key=token_key).first()
        if token:
            is_expire = self.checkout_token_time(token)
            if token and not is_expire:  # 没过期
                return {'user': token.user, 'result': True}
            else:
                return {'user': None, 'result': False}
        else:
            return {'user': None, 'result': False}
    

    def checkout_token_time(self, token):
        today = localtime()
        past_due = token.created + datetime.timedelta(days=+settings.TOKEN_AGE)
        if today > past_due:
            return True # 过期
        return False # 没过期