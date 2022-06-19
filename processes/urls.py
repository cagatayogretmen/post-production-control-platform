from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('population-chart/', views.population_chart, name='population-chart'),
    
    path('create_process/', views.process_create_main, name = 'create-process-main'),
    path('user_profile/', views.user_profile, name = 'user-profile'),
    path('pdf_1/<int:pk>', views.pdf_sticker, name = 'pdf-1'),
    path('pdf_2/<int:pk>', views.pdf_sticker2, name = 'pdf-2'),
    path('pdf_3/<int:pk>', views.pdf_sticker3, name = 'pdf-3'),
    path('pdf_adres/<int:pk>', views.pdf_fonksiyon, name = 'pdf_ismi'),

    #raporlar sayfası
    path('reports/', views.reports, name= 'reports'),

    #product urls
    path('list_product/', views.product_list, name='list-product'),
    path('create_product/', views.product_create, name = 'create-product'),
    path('detail_product/<int:pk>', views.product_detail, name = 'detail-product'),
    path('update_product/<int:pk>', views.product_update, name = 'update-product'),
    path('delete_product/<int:pk>/', views.product_delete, name = 'delete-product'),
    path('info_product/<int:pk>', views.product_info, name = 'info-product'),

    #process1 urls
    path('list_process1/', views.process1_list, name='list-process1'),
    path('create_process1/<int:pk>', views.process1_create, name='create-process1'),
    path('detail_process1/<int:pk>/', views.process1_detail, name='detail-process1'),
    path('update_process1/<int:pk>', views.process1_update, name='update-process1'),
    path('delete_process1/<int:pk>', views.process1_delete, name='delete-process1'),

    #process1_2 urls
    path('list_process1_2/', views.process1_2_list, name='list-process1_2'),
    path('create_process1_2/', views.process1_2_create, name='create-process1_2'),
    path('detail_process1_2/<int:pk>', views.process1_2_detail, name='detail-process1_2'),
    path('update_process1_2/<int:pk>', views.process1_2_update, name='update-process1_2'),
    path('delete_process1_2/<int:pk>', views.process1_2_delete, name='delete-process1_2'),    

    #process2_2 urls
    path('list_process2_2/', views.process2_2_list, name='list-process2_2'),
    path('create_process2_2/', views.process2_2_create, name='create-process2_2'),
    path('detail_process2_2/<int:pk>', views.process2_2_detail, name='detail-process2_2'),
    path('update_process2_2/<int:pk>', views.process2_2_update, name='update-process2_2'),
    path('delete_process2_2/<int:pk>', views.process2_2_delete, name='delete-process2_2'),

    #process3_2 urls
    path('list_process3_2/', views.process3_2_list, name='list-process3_2'),
    path('create_process3_2/', views.process3_2_create, name='create-process3_2'),
    path('detail_process3_2/<int:pk>', views.process3_2_detail, name='detail-process3_2'),
    path('update_process3_2/<int:pk>', views.process3_2_update, name='update-process3_2'),
    path('delete_process3_2/<int:pk>', views.process3_2_delete, name='delete-process3_2'),

    #process4_2 urls
    path('list_process4_2/', views.process4_2_list, name='list-process4_2'),
    path('create_process4_2/', views.process4_2_create, name='create-process4_2'),
    path('detail_process4_2/<int:pk>', views.process4_2_detail, name='detail-process4_2'),
    path('update_process4_2/<int:pk>', views.process4_2_update, name='update-process4_2'),
    path('delete_process4_2/<int:pk>', views.process4_2_delete, name='delete-process4_2'),

    #process5_2 urls
    path('list_process5_2/', views.process5_2_list, name='list-process5_2'),
    path('create_process5_2/', views.process5_2_create, name='create-process5_2'),
    path('detail_process5_2/<int:pk>', views.process5_2_detail, name='detail-process5_2'),
    path('update_process5_2/<int:pk>', views.process5_2_update, name='update-process5_2'),
    path('delete_process5_2/<int:pk>', views.process5_2_delete, name='delete-process5_2'),

    #process6_2 urls
    path('list_process6_2/', views.process6_2_list, name='list-process6_2'),
    path('create_process6_2/', views.process6_2_create, name='create-process6_2'),
    path('detail_process6_2/<int:pk>', views.process6_2_detail, name='detail-process6_2'),
    path('update_process6_2/<int:pk>', views.process6_2_update, name='update-process6_2'),
    path('delete_process6_2/<int:pk>', views.process6_2_delete, name='delete-process6_2'),

    #process7_2 urls
    path('list_process7_2/', views.process7_2_list, name='list-process7_2'),
    path('create_process7_2/', views.process7_2_create, name='create-process7_2'),
    path('detail_process7_2/<int:pk>', views.process7_2_detail, name='detail-process7_2'),
    path('update_process7_2/<int:pk>', views.process7_2_update, name='update-process7_2'),
    path('delete_process7_2/<int:pk>', views.process7_2_delete, name='delete-process7_2'),

    #process8_2 urls
    path('list_process8_2/', views.process8_2_list, name='list-process8_2'),
    path('create_process8_2/', views.process8_2_create, name='create-process8_2'),
    path('detail_process8_2/<int:pk>', views.process8_2_detail, name='detail-process8_2'),
    path('update_process8_2/<int:pk>', views.process8_2_update, name='update-process8_2'),
    path('delete_process8_2/<int:pk>', views.process8_2_delete, name='delete-process8_2'),

    #process1 urls
    path('list_process1/', views.process1_list, name='list-process1'),
    path('create_process1/', views.process1_create, name='create-process1'),
    path('detail_process1/<int:pk>', views.process1_detail, name='detail-process1'),
    path('update_process1/<int:pk>', views.process1_update, name='update-process1'),
    path('delete_process1/<int:pk>', views.process1_delete, name='delete-process1'),
    path('info_process1/<int:pk>', views.process1_info, name='info-process1'),

    #process2 urls
    path('list_process2/', views.process2_list, name='list-process2'),
    path('create_process2/', views.process2_create, name='create-process2'),
    path('detail_process2/<int:pk>', views.process2_detail, name='detail-process2'),
    path('update_process2/<int:pk>', views.process2_update, name='update-process2'),
    path('delete_process2/<int:pk>', views.process2_delete, name='delete-process2'),
    path('info_process2/<int:pk>', views.process2_info, name='info-process2'),

    #process3 urls
    path('list_process3/', views.process3_list, name='list-process3'),
    path('create_process3/', views.process3_create, name='create-process3'),
    path('detail_process3/<int:pk>', views.process3_detail, name='detail-process3'),
    path('update_process3/<int:pk>', views.process3_update, name='update-process3'),
    path('delete_process3/<int:pk>', views.process3_delete, name='delete-process3'),
    path('info_process3/<int:pk>', views.process3_info, name='info-process3'),

    #process4 urls
    path('list_process4/', views.process4_list, name='list-process4'),
    path('create_process4/', views.process4_create, name='create-process4'),
    path('detail_process4/<int:pk>', views.process4_detail, name='detail-process4'),
    path('update_process4/<int:pk>', views.process4_update, name='update-process4'),
    path('delete_process4/<int:pk>', views.process4_delete, name='delete-process4'),
    path('info_process4/<int:pk>', views.process4_info, name='info-process4'),

    #process5 urls
    path('list_process5/', views.process5_list, name='list-process5'),
    path('create_process5/', views.process5_create, name='create-process5'),
    path('detail_process5/<int:pk>', views.process5_detail, name='detail-process5'),
    path('update_process5/<int:pk>', views.process5_update, name='update-process5'),
    path('delete_process5/<int:pk>', views.process5_delete, name='delete-process5'),
    path('info_process5/<int:pk>', views.process5_info, name='info-process5'),

    #process6 urls
    path('list_process6/', views.process6_list, name='list-process6'),
    path('create_process6/', views.process6_create, name='create-process6'),
    path('detail_process6/<int:pk>', views.process6_detail, name='detail-process6'),
    path('update_process6/<int:pk>', views.process6_update, name='update-process6'),
    path('delete_process6/<int:pk>', views.process6_delete, name='delete-process6'),
    path('info_process6/<int:pk>', views.process6_info, name='info-process6'),

    #process7 urls
    path('list_process7/', views.process7_list, name='list-process7'),
    path('create_process7/', views.process7_create, name='create-process7'),
    path('detail_process7/<int:pk>', views.process7_detail, name='detail-process7'),
    path('update_process7/<int:pk>', views.process7_update, name='update-process7'),
    path('delete_process7/<int:pk>', views.process7_delete, name='delete-process7'),
    path('info_process7/<int:pk>', views.process7_info, name='info-process7'),

    #process8 urls
    path('list_process8/', views.process8_list, name='list-process8'),
    path('create_process8/', views.process8_create, name='create-process8'),
    path('detail_process8/<int:pk>', views.process8_detail, name='detail-process8'),
    path('update_process8/<int:pk>', views.process8_update, name='update-process8'),
    path('delete_process8/<int:pk>', views.process8_delete, name='delete-process8'),
    path('info_process8/<int:pk>', views.process8_info, name='info-process8'),
    ]

if settings.DEBUG: 
         urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
                               