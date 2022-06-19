from django import forms
from .models import (Product, Process_1 ,Process_2, Process_3, Process_4, Process_5, Process_6, Process_7, Process_8, Process_1_2 ,Process_2_2, Process_3_2, Process_4_2, Process_5_2, Process_6_2, Process_7_2, Process_8_2)
from django.contrib.auth.models import User
from django.db import models

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude =['slug','created_by', "order_date"]
class Process1Form(forms.ModelForm):
    class Meta:
        model = Process_1
        exclude =['slug','created_by']
class Process2Form(forms.ModelForm):
    class Meta:
        model = Process_2
        exclude =['slug','created_by']
class Process3Form(forms.ModelForm):
    class Meta:
        model = Process_3
        exclude =['slug','created_by']
class Process4Form(forms.ModelForm):
    class Meta:
        model = Process_4
        exclude =['slug','created_by']
class Process5Form(forms.ModelForm):
    class Meta:
        model = Process_5
        exclude =['slug','created_by']
class Process6Form(forms.ModelForm):
    class Meta:
        model = Process_6
        exclude =['slug','created_by']
class Process7Form(forms.ModelForm):
    class Meta:
        model = Process_7
        exclude =['slug','created_by']
class Process8Form(forms.ModelForm):
    class Meta:
        model = Process_8
        exclude =['slug','created_by']


class Process1_2Form(forms.ModelForm):
    class Meta:
        model = Process_1_2
        exclude =['slug','created_by']
class Process2_2Form(forms.ModelForm):
    class Meta:
        model = Process_2_2
        exclude =['slug','created_by']
class Process3_2Form(forms.ModelForm):
    class Meta:
        model = Process_3_2
        exclude =['slug','created_by']
class Process4_2Form(forms.ModelForm):
    class Meta:
        model = Process_4_2
        exclude =['slug','created_by']
class Process5_2Form(forms.ModelForm):
    class Meta:
        model = Process_5_2
        exclude =['slug','created_by']
class Process6_2Form(forms.ModelForm):
    class Meta:
        model = Process_6_2
        exclude =['slug','created_by']
class Process7_2Form(forms.ModelForm):
    class Meta:
        model = Process_7_2
        exclude =['slug','created_by']
class Process8_2Form(forms.ModelForm):
    class Meta:
        model = Process_8_2
        exclude =['slug','created_by']