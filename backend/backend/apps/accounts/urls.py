from django.urls import path
from .views import UserList, UserDetail, LoginView, userLogout, getToken
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('users/', UserList.as_view(), name="user-list"),
    path('users/<int:pk>/', UserDetail.as_view(), name="user-detail"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', userLogout, name="logout"),
    path('get-token', getToken, name='get-token')
])

