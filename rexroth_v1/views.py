from django.shortcuts import render

def login(request):
    context = {

    }

    return render(request, 'home.html', context=context)