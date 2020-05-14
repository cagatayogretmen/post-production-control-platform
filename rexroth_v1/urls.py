
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views
from .views import GeneratePDF


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('processes.urls')),
    path('accounts/', include('accounts.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('pdf/', GeneratePDF.as_view()),

    ]

admin.site.site_header = "Rexroth Kalite Kontrol Uygulaması "
admin.site.site_title = "Rexroth Kalite Kontrol Uygulaması"
admin.site.index_title = "Anasayfa"