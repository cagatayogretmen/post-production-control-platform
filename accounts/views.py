from django.shortcuts import render,HttpResponseRedirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from .models import UserProfile
from django.contrib.auth.models import User

def user_login(request):
    if not request.user.is_anonymous:
        return HttpResponseRedirect(reverse('home'))
        
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                msg = '<b>Merhaba</b>'
                return HttpResponseRedirect(reverse('home'))

    return render(request, 'login.html', context = {'form':form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user-login'))
 
