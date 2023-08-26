import datetime, jwt, time
from django.utils.timezone import localtime
from django.conf import settings
from rest_framework.authtoken.models import Token


def generation_token(user_id: int) -> str:
    expire_time =  int(time.time()) + 3600*24*settings.TOKEN_AGE
    token = jwt.encode(
        payload={'user_id': user_id, 'exp_time': expire_time},
        key=settings.SECRET_KEY, 
        algorithm='HS256'
    )
    return token

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


def login_require(request):
    try:
        token = request.META['HTTP_AUTHORIZATION']
        if checkout_token_time(token, request):
            # token 过期， 需要登录
            return True
    except Exception as e:
        # 需要token验证 但是传入没有token， 则需要登录
        request.data["need_login"] = True
        return True
    return False