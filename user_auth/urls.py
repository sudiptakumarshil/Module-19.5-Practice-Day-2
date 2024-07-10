from django.urls import path
from .views import *

urlpatterns = [
    path('user/register', UserRegistrationView.as_view(), name='user.register'),
    path('user/login', UserLoginView.as_view(), name='user.login'),
    path('user/logout', UserLogoutView.as_view(), name='user.logout')
]
