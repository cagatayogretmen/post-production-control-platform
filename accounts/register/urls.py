from django.conf.urls import url
from .views import register,user_login, user_logout, user_profile

urlpatterns = [
    url('register', view = register, name = 'register'),
    url('login', view = user_login, name = 'user-login'),
    url('logout', view = user_logout, name = 'user-logout'),
    url('sayfa', view = user_profile, name = 'foto'),
]