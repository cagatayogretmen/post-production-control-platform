from .models import Product, Process_1, Process_2, Process_3, Process_4, Process_5, Process_6, Process_7, Process_8
from .forms import ProductForm, Process1Form, Process1Form_2, Process2Form, Process2Form_2, Process3Form, Process4Form, Process5Form, Process6Form, Process7Form, Process8Form
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from accounts.models import UserProfile
from django.contrib.auth.models import User
#başlangıç
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf
from django import template
from django.contrib.auth.models import Group





class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('report.html')
        context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('report.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
#bitiş

def pdf_create(request):
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


'''
    login required için diğer yöntem

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('user-login'))
'''


@login_required
def index(request):

    #ürün adeti hesaplama fonksiyonu
    adet = 0 
    for i in Product.objects.all():
        adet = adet+1

    context = {
        "adet": adet,
    }

    return render(request, 'index.html', context=context)



@login_required
def user_profile(request):

    return render(request, 'profil.html', context = {})


@login_required
def process_create_main(request):
    context = {
    }

    return render(request, 'product/create_process_main.html', context = context)



#------ Product ------# 

@login_required
def product_list(request):
    context = {
        "all_products" : Product.objects.all(),
        "name" : 'Ürün Listesi',
    }

    return render(request, 'product/list_product.html', context=context)

@login_required
def product_create(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(data = request.POST)
        if form.is_valid():            
            form.save()
            return HttpResponseRedirect(reverse('list-product'))

    return render(request, 'product/create_product.html', context = {'form':form})

@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    #1.süreç
    if Process_1.objects.filter(product__product_name = product.product_name):
        process1 = Process_1.objects.get(product__product_name = product.product_name)
        deger_1 = 1
    else:
        process1 = ''
        deger_1 = 0

    #2.süreç
    if Process_2.objects.filter(product__product_name = product.product_name):
        process2 = Process_2.objects.get(product__product_name = product.product_name)
        deger_2 = 1
    else:
        process2 = ''
        deger_2 = 0  

    #3.süreç
    if Process_3.objects.filter(product__product_name = product.product_name):
        process3 = Process_3.objects.get(product__product_name = product.product_name)
        deger_3 = 1
    else:
        process3 = ''
        deger_3 = 0

    #4.süreç
    if Process_4.objects.filter(product__product_name = product.product_name):
        process4 = Process_4.objects.get(product__product_name = product.product_name)
        deger_4 = 1
    else:
        process4 = ''
        deger_4 = 0 

    #5.süreç
    if Process_5.objects.filter(product__product_name = product.product_name):
        process5 = Process_5.objects.get(product__product_name = product.product_name)
        deger_5 = 1
    else:
        process5 = ''
        deger_5 = 0  

    #6.süreç
    if Process_6.objects.filter(product__product_name = product.product_name):
        process6 = Process_6.objects.get(product__product_name = product.product_name)
        deger_6 = 1
    else:
        process6 = ''
        deger_6 = 0

    #7.süreç
    if Process_7.objects.filter(product__product_name = product.product_name):
        process7 = Process_7.objects.get(product__product_name = product.product_name)
        deger_7 = 1
    else:
        process7 = ''
        deger_7 = 0 

    #7.süreç
    if Process_8.objects.filter(product__product_name = product.product_name):
        process8 = Process_8.objects.get(product__product_name = product.product_name)
        deger_8 = 1
    else:
        process8 = ''
        deger_8 = 0 


    context = {
        'product' : product,
        'process1' : process1,
        'process2' : process2,
        'process3' : process3,
        'process4' : process4,
        'process5' : process5,
        'process6' : process6,
        'process7' : process7,
        'process8' : process8,
        'deger_1' : deger_1,
        'deger_2' : deger_2,  
        'deger_3' : deger_3,   
        'deger_4' : deger_4,
        'deger_5' : deger_5,  
        'deger_6' : deger_6, 
        'deger_7' : deger_7, 
        'deger_8' : deger_8,
    }

    return render(request, 'product/detail_product.html', context = context )

@login_required
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

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return HttpResponseRedirect(reverse('list-product'))
    


#------ Process1 ------# 

create_1 = 'Ön Montaj Süreci Oluştur'
create_2 = ''
create_3 = ''

@login_required
def process1_create(request):
    form = Process1Form()

    if request.method == 'POST':
        form = Process1Form(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-process1'))

    return render(request, 'process1/create_process.html', context = {'form':form, 'text':'create_1'})

def process1_create_2(request):
    form = Process1Form_2()
    if request.method == 'POST':
        form = Process1Form_2(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-process1'))
    return render(request, 'process1/create_2.html', context ={'form':form, 'text':'deneme'} )

@login_required
def process1_detail(request, pk):

    process = get_object_or_404(Process_1, pk=pk)
    product = Product.objects.get(product_name = process.product)



    context = {
        'process' : process,
        'product' : product,

    }

    return render(request, 'process1/detail_process.html', context = context )

@login_required
def process1_update(request, pk):
    process = get_object_or_404(Process_1, pk=pk)
    form = Process1Form_2(instance=process, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process1'))


    context = {
        'process' : process,
        'form' : form,
    }

    return render(request, 'process1/update_process.html', context=context)

@login_required
def process1_delete(request, pk):
    process = get_object_or_404(Process_1, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process1'))

@login_required
def process1_list(request):
    context = {
        'title' : 'Süreç Listesi',
        "all_processes" : Process_1.objects.all(),

    }

    return render(request, 'process1/list_process.html', context=context)



#------ Process2 ------# 

@login_required
def process2_create(request):
    form = Process2Form()

    if request.method == 'POST':
        form = Process2Form(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-process2'))

    return render(request, 'process2/create_process.html', context = {'form':form})

def process2_create_2(request):
    form = Process2Form_2()
    if request.method == 'POST':
        form = Process2Form_2(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-process1'))
    return render(request, 'process2/create_2.html', context ={'form':form, 'text':'deneme'} )    

@login_required
def process2_detail(request, pk):
    process = get_object_or_404(Process_2, pk=pk)
    product = Product.objects.get(product_name = process.product)

    context = {
        'process' : process,
        'product' : product,

    }

    return render(request, 'process2/detail_process.html', context = context )

@login_required
def process2_update(request, pk):
    process = get_object_or_404(Process_2, pk=pk)
    form = Process2Form(instance=process, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process2'))


    context = {
        'process' : process,
        'form' : form,
    }

    return render(request, 'process2/update_process.html', context=context)

@login_required
def process2_delete(request, pk):
    process = get_object_or_404(Process_2, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process2'))

@login_required
def process2_list(request):
    context = {
        'title' : 'Süreç Listesi',
        "all_processes" : Process_2.objects.all(),

    }

    return render(request, 'process2/list_process.html', context=context)





#------ Process3 ------# 

@login_required
def process3_create(request):
    form = Process3Form()

    if request.method == 'POST':
        form = Process3Form(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-process3'))

    return render(request, 'process3/create_process.html', context = {'form':form})

@login_required
def process3_detail(request, pk):
    process = get_object_or_404(Process_3, pk=pk)
    product = Product.objects.get(product_name = process.product)


    context = {
        'process' : process,
        'product' : product,

    }

    return render(request, 'process3/detail_process.html', context = context )

@login_required
def process3_update(request, pk):
    process = get_object_or_404(Process_3, pk=pk)
    form = Process3Form(instance=process, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process3'))


    context = {
        'process' : process,
        'form' : form,
    }

    return render(request, 'process3/update_process.html', context=context)

@login_required
def process3_delete(request, pk):
    process = get_object_or_404(Process_3, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process3'))

@login_required
def process3_list(request):
    context = {
        'title' : 'Süreç Listesi',
        "all_processes" : Process_3.objects.all(),

    }

    return render(request, 'process3/list_process.html', context=context)



#------ Process4 ------# 

@login_required
def process4_create(request):
    form = Process4Form()

    if request.method == 'POST':
        form = Process4Form(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-process4'))

    return render(request, 'process4/create_process.html', context = {'form':form})

@login_required
def process4_detail(request, pk):
    process = get_object_or_404(Process_4, pk=pk)
    product = Product.objects.get(product_name = process.product)


    context = {
        'process' : process,
        'product' : product,

    }

    return render(request, 'process4/detail_process.html', context = context )

@login_required
def process4_update(request, pk):
    process = get_object_or_404(Process_4, pk=pk)
    form = Process4Form(instance=process, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process4'))


    context = {
        'process' : process,
        'form' : form,
    }

    return render(request, 'process4/update_process.html', context=context)

@login_required
def process4_delete(request, pk):
    process = get_object_or_404(Process_4, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process4'))

@login_required
def process4_list(request):
    context = {
        'title' : 'Süreç Listesi',
        "all_processes" : Process_4.objects.all(),

    }

    return render(request, 'process4/list_process.html', context=context)

#------ Process5 ------# 

@login_required
def process5_create(request):
    form = Process5Form()

    if request.method == 'POST':
        form = Process5Form(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-process5'))

    return render(request, 'process5/create_process.html', context = {'form':form})

@login_required
def process5_detail(request, pk):
    process = get_object_or_404(Process_5, pk=pk)
    product = Product.objects.get(product_name = process.product)


    context = {
        'process' : process,
        'product' : product,

    }

    return render(request, 'process5/detail_process.html', context = context )

@login_required
def process5_update(request, pk):
    process = get_object_or_404(Process_5, pk=pk)
    form = Process5Form(instance=process, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process5'))


    context = {
        'process' : process,
        'form' : form,
    }

    return render(request, 'process5/update_process.html', context=context)

@login_required
def process5_delete(request, pk):
    process = get_object_or_404(Process_5, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process5'))

@login_required
def process5_list(request):
    context = {
        'title' : 'Süreç Listesi',
        "all_processes" : Process_5.objects.all(),

    }

    return render(request, 'process5/list_process.html', context=context)

#------ Process6 ------# 

@login_required
def process6_create(request):
    form = Process6Form()

    if request.method == 'POST':
        form = Process6Form(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-process6'))

    return render(request, 'process6/create_process.html', context = {'form':form})

@login_required
def process6_detail(request, pk):
    process = get_object_or_404(Process_6, pk=pk)
    product = Product.objects.get(product_name = process.product)


    context = {
        'process' : process,
        'product' : product,

    }

    return render(request, 'process6/detail_process.html', context = context )

@login_required
def process6_update(request, pk):
    process = get_object_or_404(Process_6, pk=pk)
    form = Process6Form(instance=process, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process6'))


    context = {
        'process' : process,
        'form' : form,
    }

    return render(request, 'process6/update_process.html', context=context)

@login_required
def process6_delete(request, pk):
    process = get_object_or_404(Process_6, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process6'))

@login_required
def process6_list(request):
    context = {
        'title' : 'Süreç Listesi',
        "all_processes" : Process_6.objects.all(),

    }

    return render(request, 'process6/list_process.html', context=context)

#------ Process7 ------# 

@login_required
def process7_create(request):
    form = Process7Form()

    if request.method == 'POST':
        form = Process7Form(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-process7'))

    return render(request, 'process7/create_process.html', context = {'form':form})

@login_required
def process7_detail(request, pk):
    process = get_object_or_404(Process_7, pk=pk)
    product = Product.objects.get(product_name = process.product)


    context = {
        'process' : process,
        'product' : product,

    }

    return render(request, 'process7/detail_process.html', context = context )

@login_required
def process7_update(request, pk):
    process = get_object_or_404(Process_7, pk=pk)
    form = Process7Form(instance=process, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process7'))


    context = {
        'process' : process,
        'form' : form,
    }

    return render(request, 'process7/update_process.html', context=context)

@login_required
def process7_delete(request, pk):
    process = get_object_or_404(Process_7, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process7'))

@login_required
def process7_list(request):
    context = {
        'title' : 'Süreç Listesi',
        "all_processes" : Process_7.objects.all(),

    }

    return render(request, 'process7/list_process.html', context=context)





#------ Process8 ------# 

@login_required
def process8_create(request):
    form = Process8Form()

    if request.method == 'POST':
        form = Process8Form(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-process8'))

    return render(request, 'process8/create_process.html', context = {'form':form})

@login_required
def process8_detail(request, pk):
    process = get_object_or_404(Process_8, pk=pk)
    product = Product.objects.get(product_name = process.product)

    context = {
        'process' : process,
        'product' : product,

    }

    return render(request, 'process8/detail_process.html', context = context )

@login_required
def process8_update(request, pk):
    process = get_object_or_404(Process_8, pk=pk)
    form = Process8Form(instance=process, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process8'))


    context = {
        'process' : process,
        'form' : form,
    }

    return render(request, 'process8/update_process.html', context=context)

@login_required
def process8_delete(request, pk):
    process = get_object_or_404(Process_8, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process8'))

@login_required
def process8_list(request):
    context = {
        'title' : 'Süreç Listesi',
        "all_processes" : Process_8.objects.all(),

    }

    return render(request, 'process8/list_process.html', context=context)



    