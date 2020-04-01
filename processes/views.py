from django.shortcuts import render
from .models import Product, Process_first, Process_second, Process_three

def index(request):
    context = {

    }

    return render(request, 'index.html', context=context)

def new_product(request):
    context = {

    }

    return render(request, 'new_product.html', context = context)

def new_process(request):
    context = {

    }

    return render(request, 'new_process.html', context = context)