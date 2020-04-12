from django import forms
from .models import Product, Process_1 ,Process_2, Process_3, Process_4, Process_5, Process_6, Process_7


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ()

class Process1Form(forms.ModelForm):
    class Meta:
        model = Process_1
        exclude = ()

class Process2Form(forms.ModelForm):
    class Meta:
        model = Process_2
        exclude = ()

class Process3Form(forms.ModelForm):
    class Meta:
        model = Process_3
        exclude = ()
class Process4Form(forms.ModelForm):
    class Meta:
        model = Process_4
        exclude = ()

class Process5Form(forms.ModelForm):
    class Meta:
        model = Process_5
        exclude = ()

class Process6Form(forms.ModelForm):
    class Meta:
        model = Process_6
        exclude = ()
class Process7Form(forms.ModelForm):
    class Meta:
        model = Process_7
        exclude = ()