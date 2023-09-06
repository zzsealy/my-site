
from django.urls import path
from .views import LoginView, UserRegister, UserInfo
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    # path('users/', UserList.as_view(), name="user-list"),
    # path('users/<int:pk>/', UserDetail.as_view(), name="user_detail"),
    # path('get-token', getToken, name='get_token'),
    # path('users/logout', userLogout, name="logout"),
    path('users/login', LoginView.as_view(), name="login"),
    path('users/register', UserRegister.as_view(), name='user_register'),
    path('users/user_info', UserInfo.as_view(), name='user_info')
])