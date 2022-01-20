import datetime
from django.utils.timezone import localtime
from django.conf import settings
from rest_framework.authtoken.models import Token


def checkout_token_time(token_key, request): 
    token = Token.objects.filter(key=token_key).first()
    today = localtime()
    request.user = token.user
    past_due = token.created + datetime.timedelta(days=+settings.TOKEN_AGE)
    if today > past_due:
        return True # 过期
    return False # 没过期



def login_expire(func):
    def wrapper(request, *args, **kwargs):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            if checkout_token_time(token, request):
                # token 过期， 需要登录
                request.data["need_login"] = True
        except Exception as e:
            # 需要token验证 但是传入没有token， 则需要登录
            request.data["need_login"] = True
            print("error:", e)
        return func(request, *args, **kwargs)
    return wrapper