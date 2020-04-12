from django.contrib import admin
from .models import Product, Process_1, Process_2, Process_3, Process_4, Process_5, Process_6, Process_7


class Product_list(admin.ModelAdmin):
    list_display = ('product_name', 'slug', 'status','created_on','production_order_no','order_position_no','quantity')
    list_filter = ("status",'created_by','created_on')
    search_fields = ['product_name', 'content']
    prepopulated_fields = {'slug': ('product_name',)}

class Process_list_1(admin.ModelAdmin):
    list_display = ('product', 'slug', 'status','created_on')
    list_filter = ("status",'created_by','created_on')
    search_fields = ['product', 'content']
    prepopulated_fields = {'slug': ('product',)}

class Process_list_2(admin.ModelAdmin):
    list_display = ('product', 'slug', 'status','created_on')
    list_filter = ("status",'created_by','created_on')
    search_fields = ['product', 'content']
    prepopulated_fields = {'slug': ('product',)}

class Process_list_3(admin.ModelAdmin):
    list_display = ('product', 'slug', 'status','created_on')
    list_filter = ("status",'created_by','created_on')
    search_fields = ['product', 'content']
    prepopulated_fields = {'slug': ('product',)}

class Process_list_4(admin.ModelAdmin):
    list_display = ('product', 'slug', 'status','created_on')
    list_filter = ("status",'created_by','created_on')
    search_fields = ['product', 'content']
    prepopulated_fields = {'slug': ('product',)}

class Process_list_5(admin.ModelAdmin):
    list_display = ('product', 'slug', 'status','created_on')
    list_filter = ("status",'created_by','created_on')
    search_fields = ['product', 'content']
    prepopulated_fields = {'slug': ('product',)}

class Process_list_6(admin.ModelAdmin):
    list_display = ('product', 'slug', 'status','created_on')
    list_filter = ("status",'created_by','created_on')
    search_fields = ['product', 'content']
    prepopulated_fields = {'slug': ('product',)}

class Process_list_7(admin.ModelAdmin):
    list_display = ('product', 'slug', 'status','created_on')
    list_filter = ("status",'created_by','created_on')
    search_fields = ['product', 'content']
    prepopulated_fields = {'slug': ('product',)}


admin.site.register(Product, Product_list)
admin.site.register(Process_1, Process_list_1)
admin.site.register(Process_2, Process_list_2)
admin.site.register(Process_3, Process_list_3)
admin.site.register(Process_4, Process_list_4)
admin.site.register(Process_5, Process_list_5)
admin.site.register(Process_6, Process_list_6)
admin.site.register(Process_7, Process_list_7)







