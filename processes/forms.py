from django import forms
from .models import Product, Process_1 ,Process_2, Process_3, Process_4, Process_5, Process_6, Process_7, Process_8
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name','status')
'''
    def clean_author(self):
        if not self.cleaned_data['created_by']:
            return User()
        return self.cleaned_data['created_by']
'''

class Process1Form(forms.ModelForm):
    class Meta:
        model = Process_1
        fields = ('product','status','created_by','slug','soru1')

class Process1Form_2(forms.ModelForm):
    class Meta:
        model = Process_1
        fields = ('soru2','soru3')

#process2
class Process2Form(forms.ModelForm):
    class Meta:
        model = Process_2
        fields = ('product','status','created_by', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14',
         'q15', 'q16', 'q17', 'q18', 'q19', 'q20',
         'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34')

class Process2Form_2(forms.ModelForm):
    class Meta:
        model = Process_2
        fields = ('q35', 'q36', 'q37', 'q38', 'q39', 'q40', 'q41', 'q42', 'q43', 'q44', 'q45',
         'q46', 'q47', 'q48', 'q49', 'q50', 'q51', 'q52')

#process 3
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
class Process8Form(forms.ModelForm):
    class Meta:
        model = Process_8
        exclude = ()