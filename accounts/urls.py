from django.conf.urls import url
from .views import user_login, user_logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('login', view = user_login, name = 'user-login'),
    url('logout', view = user_logout, name = 'user-logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)