from django.shortcuts import render,HttpResponseRedirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
#from .models import UserProfile


def register(request):
    if not request.user.is_anonymous:
        return HttpResponseRedirect(reverse('home'))

    form = RegisterForm(data = request.POST or None)


    if form.is_valid():
        user = form.save(commit = False)
        password = form.cleaned_data.get('password')
        username = form.cleaned_data.get('username')
        user.set_password(password)
        user.save()
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, '<b<Tebrikler Kayıt oldunuz</b>', extra_tags='success')
                return HttpResponseRedirect(reverse('home'))

    return render(request, 'register.html', context = {'form':form})

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
 
def user_profile(request):

    return render(request, 'profil.html', context = {})