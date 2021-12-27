import datetime
from django.utils.timezone import localtime
from django.conf import settings
from rest_framework.authtoken.models import Token


def checkout_token_time(token_key): 
    token = Token.objects.filter(key=token_key).first()
    today = localtime()
    past_due = token.created + datetime.timedelta(days=+settings.TOKEN_AGE)
    if today > past_due:
        return True # 没过期
    return False # 过期



def login_required(func):
    def wrapper(request, *args, **kwargs):
        try:
            token = request.META['HTTP_AUTHORIZATION']
            if checkout_token_time(token):
                request.data["need_login"] = True
        except Exception as e:
            print("error:", e)
        return func(request, *args, **kwargs)
    return wrapper