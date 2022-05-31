import json
import datetime

from django.conf import settings
from django.utils.timezone import localtime
from django.utils.deprecation import MiddlewareMixin
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.http import HttpResponse
from django.http import JsonResponse

class Middleware(MiddlewareMixin):

    def process_request(self, request, **kwargs):
        user = self.verify_login_validity(request)
        request.user = user
        # return JsonResponse(data={"susscess":0, "message":"记录事件开始到数据库出错"}, content_type='application/json', status=401)

    
    def verify_login_validity(self, request):
        token_key = request.META.get('HTTP_AUTHORIZATION', None)
        if not token_key:
            return None
        token = Token.objects.filter(key=token_key).first()
        is_expire = self.checkout_token_time(token)
        if token and not is_expire:
            return token.user
        return None
    

    def checkout_token_time(self, token):
        today = localtime()
        past_due = token.created + datetime.timedelta(days=+settings.TOKEN_AGE)
        if today > past_due:
            return True # 过期
        return False # 没过期