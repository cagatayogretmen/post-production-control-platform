from django import forms
from .models import Product, Process_first ,Process_second, Process_three


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ()

class Process1Form(forms.ModelForm):
    class Meta:
        model = Process_first
        exclude = ()

class Process2Form(forms.ModelForm):
    class Meta:
        model = Process_second
        exclude = ()

class Process3Form(forms.ModelForm):
    class Meta:
        model = Process_three
        exclude = ()