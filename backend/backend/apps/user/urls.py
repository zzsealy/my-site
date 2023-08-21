
from django.urls import path
from django.conf.urls import url
from .views import UserList, UserDetail, LoginView, userLogout, getToken, UserRegister
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    # path('users/', UserList.as_view(), name="user-list"),
    # path('users/<int:pk>/', UserDetail.as_view(), name="user_detail"),
    # path('get-token', getToken, name='get_token'),
    # path('users/logout', userLogout, name="logout"),
    url(r'^users/login', LoginView.as_view(), name="login"),
    url(r'^users/register$', UserRegister.as_view(), name='user_register')
])