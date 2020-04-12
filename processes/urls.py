from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [

    #main urls
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('create_process/', views.process_create_main, name = 'create-process-main'),
    
    path('create_pdf/', views.pdf_create, name = 'create-pdf'),
    
    #product urls
    path('list_product/', views.product_list, name='list-product'),
    path('create_product/', views.product_create, name = 'create-product'),
    path('detail_product/(?P<pk>[0-9]+)/$', views.product_detail, name = 'detail-product'),
    path('update_product/(?P<pk>[0-9]+)/$', views.product_update, name = 'update-product'),
    path('delete_product/(?P<pk>[0-9]+)/$', views.product_delete, name = 'delete-product'),

    #process1 urls
    path('list_process1/', views.process1_list, name='list-process1'),
    path('create_process1/', views.process1_create, name='create-process1'),
    path('detail_process1/(?P<pk>[0-9]+)/$', views.process1_detail, name='detail-process1'),
    path('update_process1/(?P<pk>[0-9]+)/$', views.process1_update, name='update-process1'),
    path('delete_process1/(?P<pk>[0-9]+)/$', views.process1_delete, name='delete-process1'),

    #process2 urls
    path('list_process2/', views.process2_list, name='list-process2'),
    path('create_process2/', views.process2_create, name='create-process2'),
    path('detail_process2/(?P<pk>[0-9]+)/$', views.process2_detail, name='detail-process2'),
    path('update_process2/(?P<pk>[0-9]+)/$', views.process2_update, name='update-process2'),
    path('delete_process2/(?P<pk>[0-9]+)/$', views.process2_delete, name='delete-process2'),

    #process3 urls
    path('list_process3/', views.process3_list, name='list-process3'),
    path('create_process3/', views.process3_create, name='create-process3'),
    path('detail_process3/(?P<pk>[0-9]+)/$', views.process3_detail, name='detail-process3'),
    path('update_process3/(?P<pk>[0-9]+)/$', views.process3_update, name='update-process3'),
    path('delete_process3/(?P<pk>[0-9]+)/$', views.process3_delete, name='delete-process3'),

    #process4 urls
    path('list_process4/', views.process4_list, name='list-process4'),
    path('create_process4/', views.process4_create, name='create-process4'),
    path('detail_process4/(?P<pk>[0-9]+)/$', views.process4_detail, name='detail-process4'),
    path('update_process4/(?P<pk>[0-9]+)/$', views.process4_update, name='update-process4'),
    path('delete_process4/(?P<pk>[0-9]+)/$', views.process4_delete, name='delete-process4'),


    #process5 urls
    path('list_process5/', views.process5_list, name='list-process5'),
    path('create_process5/', views.process5_create, name='create-process5'),
    path('detail_process5/(?P<pk>[0-9]+)/$', views.process5_detail, name='detail-process5'),
    path('update_process5/(?P<pk>[0-9]+)/$', views.process5_update, name='update-process5'),
    path('delete_process5/(?P<pk>[0-9]+)/$', views.process5_delete, name='delete-process5'),

    #process6 urls
    path('list_process6/', views.process6_list, name='list-process6'),
    path('create_process6/', views.process6_create, name='create-process6'),
    path('detail_process6/(?P<pk>[0-9]+)/$', views.process6_detail, name='detail-process6'),
    path('update_process6/(?P<pk>[0-9]+)/$', views.process6_update, name='update-process6'),
    path('delete_process6/(?P<pk>[0-9]+)/$', views.process6_delete, name='delete-process6'),

    #process7 urls
    path('list_process7/', views.process7_list, name='list-process7'),
    path('create_process7/', views.process7_create, name='create-process7'),
    path('detail_process7/(?P<pk>[0-9]+)/$', views.process7_detail, name='detail-process7'),
    path('update_process7/(?P<pk>[0-9]+)/$', views.process7_update, name='update-process7'),
    path('delete_process7/(?P<pk>[0-9]+)/$', views.process7_delete, name='delete-process7'),


    ]

