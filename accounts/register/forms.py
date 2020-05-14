from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
#from .models import UserProfile

class RegisterForm(forms.ModelForm):
    password = forms.CharField(min_length=5, required=True,label= 'Parola',  widget = forms.PasswordInput(attrs={'class': 'form-control'}))
    password_confirm = forms.CharField(required=True,label= 'Parolayı Onaylayın', widget = forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name',  'email', 'password', 'password_confirm']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
    
    def clean(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password != password_confirm:
            self.add_error('password', 'Parolalar eşleşmedi')
            self.add_error('password_confirm', 'Parolalar eşleşmedi')

        def clean_email(self):
            email = self.cleaned_data.get('email')
            email = email.lower()
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Bu mail sistemde kayıtlı')
            return email


        def clean_username(self):
            username = self.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError('Bu mail sistemde kayıtlı')
            return username

class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=50, label = 'Kullanıcı Adı', widget = forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=True, max_length=50, label = 'Parola', widget = forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username = username, password = password)
        if not user:
            raise forms.ValidationError('Hatalı giriş')