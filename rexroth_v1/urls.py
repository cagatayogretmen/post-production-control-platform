
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('processes.urls')),
    path('accounts/', include('accounts.urls')),

    ]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Rexroth App"
admin.site.site_title = "Rexroth App"
admin.site.index_title = "Admin Panel"