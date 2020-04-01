from django.contrib import admin
from .models import Process_first, Product, Process_second, Process_three


class PostAdmin_1(admin.ModelAdmin):
    list_display = ('product', 'slug', 'status','created_on')
    list_filter = ("status",'created_by','created_on')
    search_fields = ['product', 'content']
    prepopulated_fields = {'slug': ('product',)}

class PostAdmin_2(admin.ModelAdmin):
    list_display = ('product', 'slug', 'status','created_on')
    list_filter = ("status",'created_by','created_on')
    search_fields = ['product', 'content']
    prepopulated_fields = {'slug': ('product',)}

class PostAdmin_3(admin.ModelAdmin):
    list_display = ('product', 'slug', 'status','created_on')
    list_filter = ("status",'created_by','created_on')
    search_fields = ['product', 'content']
    prepopulated_fields = {'slug': ('product',)}

class PostAdmin_4(admin.ModelAdmin):
    list_display = ('product_name', 'slug', 'status','created_on','production_order_no','order_position_no','quantity')
    list_filter = ("status",'created_by','created_on')
    search_fields = ['product_name', 'content']
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product, PostAdmin_4)
admin.site.register(Process_first, PostAdmin_1)
admin.site.register(Process_second, PostAdmin_2)
admin.site.register(Process_three, PostAdmin_3)











