from django.contrib import admin

from .models import (Product, Process_1 ,Process_2, Process_3, Process_4, Process_5, Process_6, Process_7, Process_8,
Process_1_2 ,Process_2_2, Process_3_2, Process_4_2, Process_5_2, Process_6_2, Process_7_2, Process_8_2)

from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse, HttpResponseRedirect
from django.contrib.auth import authenticate

class Product_list(admin.ModelAdmin):
    list_display = ('slug','created_on')
    list_filter = ('created_by','created_on')
    search_fields = ['content']
    prepopulated_fields = {'slug': ('slug',)}

class Process_list_1(admin.ModelAdmin):
    list_display = ('product', 'slug','created_on','updated_on')
    list_filter = ('created_by','created_on')
    search_fields = ['product', 'content']
    prepopulated_fields = {'slug': ('product',)}

class Process_list_2(admin.ModelAdmin):
    list_display = ('product', 'slug','created_on','updated_on')
    list_filter = ('created_by','created_on')
    search_fields = ['product', 'content']
    prepopulated_fields = {'slug': ('product',)}

class Process_list_3(admin.ModelAdmin):
    list_display = ('product', 'slug','created_on','updated_on')
    list_filter = ('created_by','created_on')
    search_fields = ['product', 'content']
    prepopulated_fields = {'slug': ('product',)}

class Process_list_4(admin.ModelAdmin):
    list_display = ('product', 'slug','created_on')
    list_filter = ('created_by','created_on')
    search_fields = ['product', 'content']
    prepopulated_fields = {'slug': ('product',)}

class Process_list_5(admin.ModelAdmin):
    list_display = ('product', 'slug','created_on')
    list_filter = ('created_by','created_on')
    search_fields = ['product', 'content']
    prepopulated_fields = {'slug': ('product',)}

class Process_list_6(admin.ModelAdmin):
    list_display = ('product', 'slug','created_on')
    list_filter = ('created_by','created_on')
    search_fields = ['product', 'content']
    prepopulated_fields = {'slug': ('product',)}

class Process_list_7(admin.ModelAdmin):
    list_display = ('product', 'slug','created_on')
    list_filter = ('created_by','created_on')
    search_fields = ['product', 'content']
    prepopulated_fields = {'slug': ('product',)}

class Process_list_8(admin.ModelAdmin):
    list_display = ('product', 'slug','created_on')
    list_filter = ('created_by','created_on')
    search_fields = ['product', 'content']
    prepopulated_fields = {'slug': ('product',)}

class Process_list_1_2(admin.ModelAdmin):
    list_display = ('product', 'slug','created_on','updated_on')
    list_filter = ('created_by','created_on')
    search_fields = ['product', 'content']
    prepopulated_fields = {'slug': ('product',)}

class Process_list_2_2(admin.ModelAdmin):
    list_display = ('product', 'slug','created_on','updated_on')
    list_filter = ('created_by','created_on')
    search_fields = ['product', 'content']
    prepopulated_fields = {'slug': ('product',)}

class Process_list_3_2(admin.ModelAdmin):
    list_display = ('product', 'slug','created_on','updated_on')
    list_filter = ('created_by','created_on')
    search_fields = ['product', 'content']
    prepopulated_fields = {'slug': ('product',)}

class Process_list_4_2(admin.ModelAdmin):
    list_display = ('product', 'slug','created_on')
    list_filter = ('created_by','created_on')
    search_fields = ['product', 'content']
    prepopulated_fields = {'slug': ('product',)}

class Process_list_5_2(admin.ModelAdmin):
    list_display = ('product', 'slug','created_on')
    list_filter = ('created_by','created_on')
    search_fields = ['product', 'content']
    prepopulated_fields = {'slug': ('product',)}

class Process_list_6_2(admin.ModelAdmin):
    list_display = ('product', 'slug','created_on')
    list_filter = ('created_by','created_on')
    search_fields = ['product', 'content']
    prepopulated_fields = {'slug': ('product',)}

class Process_list_7_2(admin.ModelAdmin):
    list_display = ('product', 'slug','created_on')
    list_filter = ('created_by','created_on')
    search_fields = ['product', 'content']
    prepopulated_fields = {'slug': ('product',)}

class Process_list_8_2(admin.ModelAdmin):
    list_display = ('product', 'slug','created_on')
    list_filter = ('created_by','created_on')
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
admin.site.register(Process_8, Process_list_8)


admin.site.register(Process_1_2, Process_list_1_2)
admin.site.register(Process_2_2, Process_list_2_2)
admin.site.register(Process_3_2, Process_list_3_2)
admin.site.register(Process_4_2, Process_list_4_2)
admin.site.register(Process_5_2, Process_list_5_2)
admin.site.register(Process_6_2, Process_list_6_2)
admin.site.register(Process_7_2, Process_list_7_2)
admin.site.register(Process_8_2, Process_list_8_2)


