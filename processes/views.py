from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse, HttpResponseRedirect
from .models import Product, Process_first, Process_second, Process_three
from .forms import ProductForm, Process1Form, Process2Form, Process3Form

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


def index(request):

    adet = 0 
    for i in Product.objects.all():
        adet = adet+1

    context = {

        "adet": adet


    }

    return render(request, 'index.html', context=context)

def process_create_main(request):

    context = {

    }

    return render(request, 'product/create_process_main.html', context = context)

#------ Product ------# 

def product_list(request):
    context = {
        "title" : 'Ürün Listesi',
        "all_products" : Product.objects.all(),

    }

    return render(request, 'product/list_product.html', context=context)

def product_create(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(data = request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
            return HttpResponseRedirect(reverse('list-product'))

    return render(request, 'product/create_product.html', context = {'form':form})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    #1.süreç
    if Process_first.objects.filter(product__product_name = product.product_name):
        process1 = Process_first.objects.get(product__product_name = product.product_name)
        deger_1 = 1
    else:
        process1 = ''
        deger_1 = 0

    #2.süreç
    if Process_second.objects.filter(product__product_name = product.product_name):
        process2 = Process_second.objects.get(product__product_name = product.product_name)
        deger_2 = 1
    else:
        process2 = ''
        deger_2 = 0  

    #3.süreç
    if Process_three.objects.filter(product__product_name = product.product_name):
        process3 = Process_three.objects.get(product__product_name = product.product_name)
        deger_3 = 1
    else:
        process3 = ''
        deger_3 = 0      



    context = {
        'product' : product,
        'process1' : process1,
        'process2' : process2,
        'process3' : process3,
        'deger_1' : deger_1,
        'deger_2' : deger_2,  
        'deger_3' : deger_3,     

    }

    return render(request, 'product/detail_product.html', context = context )

def product_update(request, pk):
    
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=product, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-product'))


    context = {
        'product' : product,
        'form' : form,
    }

    return render(request, 'product/update_product.html', context=context)

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return HttpResponseRedirect(reverse('list-product'))


#------ Process1 ------# 

def process1_create(request):
    form = Process1Form()

    if request.method == 'POST':
        form = Process1Form(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-process1'))

    return render(request, 'process1/create_process.html', context = {'form':form})

def process1_detail(request, pk):

    process = get_object_or_404(Process_first, pk=pk)
    product = Product.objects.get(product_name = process.product)



    context = {
        'process' : process,
        'product' : product,

    }

    return render(request, 'process1/detail_process.html', context = context )

def process1_update(request, pk):
    process = get_object_or_404(Process_first, pk=pk)
    form = Process1Form(instance=process, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process1'))


    context = {
        'process' : process,
        'form' : form,
    }

    return render(request, 'process1/update_process.html', context=context)

def process1_delete(request, pk):
    process = get_object_or_404(Process_first, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process1'))

def process1_list(request):
    context = {
        'title' : 'Süreç Listesi',
        "all_processes" : Process_first.objects.all(),

    }

    return render(request, 'process1/list_process.html', context=context)



#------ Process2 ------# 

def process2_create(request):
    form = Process2Form()

    if request.method == 'POST':
        form = Process2Form(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-process2'))

    return render(request, 'process2/create_process.html', context = {'form':form})

def process2_detail(request, pk):
    process = get_object_or_404(Process_second, pk=pk)
    product = Product.objects.get(product_name = process.product)

    context = {
        'process' : process,
        'product' : product,

    }

    return render(request, 'process2/detail_process.html', context = context )

def process2_update(request, pk):
    process = get_object_or_404(Process_second, pk=pk)
    form = Process2Form(instance=process, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process2'))


    context = {
        'process' : process,
        'form' : form,
    }

    return render(request, 'process2/update_process.html', context=context)

def process2_delete(request, pk):
    process = get_object_or_404(Process_second, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process2'))

def process2_list(request):
    context = {
        'title' : 'Süreç Listesi',
        "all_processes" : Process_second.objects.all(),

    }

    return render(request, 'process2/list_process.html', context=context)




#------ Process3 ------# 

def process3_create(request):
    form = Process3Form()

    if request.method == 'POST':
        form = Process3Form(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-process3'))

    return render(request, 'process3/create_process.html', context = {'form':form})

def process3_detail(request, pk):
    process = get_object_or_404(Process_three, pk=pk)
    product = Product.objects.get(product_name = process.product)


    context = {
        'process' : process,
        'product' : product,

    }

    return render(request, 'process3/detail_process.html', context = context )

def process3_update(request, pk):
    process = get_object_or_404(Process_three, pk=pk)
    form = Process3Form(instance=process, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process3'))


    context = {
        'process' : process,
        'form' : form,
    }

    return render(request, 'process3/update_process.html', context=context)

def process3_delete(request, pk):
    process = get_object_or_404(Process_three, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process3'))

def process3_list(request):
    context = {
        'title' : 'Süreç Listesi',
        "all_processes" : Process_three.objects.all(),

    }

    return render(request, 'process3/list_process.html', context=context)



