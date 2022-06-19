from django.conf.urls import url
from .views import user_login, user_logout
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import include

urlpatterns = [
    url('login', view = user_login, name = 'user-login'),
    url('logout', view = user_logout, name = 'user-logout'),
    url('^', include('django.contrib.auth.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)