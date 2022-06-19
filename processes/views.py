from .models import (Product, Process_1, Process_2, Process_3, Process_4, Process_5, Process_6, Process_7, Process_8,
Process_1_2, Process_2_2, Process_3_2, Process_4_2, Process_5_2, Process_6_2, Process_7_2, Process_8_2)
from .forms import (ProductForm, Process1Form,Process2Form, Process3Form, Process4Form, Process5Form, Process6Form,
 Process7Form, Process8Form,Process1_2Form, Process2_2Form, Process3_2Form, Process4_2Form, Process5_2Form,
  Process6_2Form, Process7_2Form, Process8_2Form)
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse, HttpResponseRedirect

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
import io
from django.http import FileResponse,HttpResponse
from reportlab.pdfgen import canvas
from accounts.models import UserProfile
from django.contrib.auth.models import User
#başlangıç
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf
from django import template
from django.contrib.auth.models import Group

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

### pdf için kütüphaneler
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.conf import settings


from django.http import FileResponse, Http404
from django.views.generic.detail import DetailView


def reports(request):
    all_products = Product.objects.all()
    controlled_products = []
    report1 = []
    report2 = []
    report3 = []

    for urun in all_products:
        urun_adi = str(urun)
        if Process_1_2.objects.filter(product__slug = urun_adi) and Process_7_2.objects.filter(product__slug = urun_adi) and Process_8_2.objects.filter(product__slug = urun_adi):
            r1 = "../pdf_1/{pk}".format(pk = urun.pk)
            r2 = "../pdf_2/{pk}".format(pk = urun.pk)
            r3 = "../pdf_3/{pk}".format(pk = urun.pk)
            report1.append(r1)   
            report2.append(r2)
            report3.append(r3)
            controlled_products.append(urun_adi)
    data = zip(controlled_products, report1,report2, report3)

    context = {
        "name": "Reports",
        "data": data,
    }

    return render(request, 'reports/report.html', context=context)



def pdf_fonksiyon(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {

    }
    return render(request, 'pdf/deneme1.html', context=context)    

##################pdf kütüphaneleri#####################

def pdf_sticker(request, pk):
    product = get_object_or_404(Product, pk=pk)
    Process7 = Process_7.objects.get(product__slug = product.slug)
    Process8 = Process_8.objects.get(product__slug = product.slug)
    Process8_2 = Process_8_2.objects.get(product__slug = product.slug)
    testname = Process7.created_by.first_name + " " + Process7.created_by.last_name
    montajname = Process8.created_by.first_name + " " + Process8.created_by.last_name
    

    if Process8.q1 == 0:
        Process8.q1 = "OK"
    if Process8.q1 == 1:
        Process8.q1 = " RED"
    if Process8.q1 == 2:
        Process8.q1 = " OUT OF SCOPE"
    if Process8.q2 == 0:
        Process8.q2 = "OK"
    if Process8.q2 == 1:
        Process8.q2 = " RED"
    if Process8.q2 == 2:
        Process8.q2 = " OUT OF SCOPE"
    if Process8.q3 == 0:
        Process8.q3 = "OK"
    if Process8.q3 == 1:
        Process8.q3 = " RED"
    if Process8.q3 == 2:
        Process8.q3 = " OUT OF SCOPE"
    if Process8.q4 == 0:
        Process8.q4 = "OK"
    if Process8.q4 == 1:
        Process8.q4 = " RED"
    if Process8.q4 == 2:
        Process8.q4 = " OUT OF SCOPE"
    if Process8.q5 == 0:
        Process8.q5 = "OK"
    if Process8.q5 == 1:
        Process8.q5 = " RED"
    if Process8.q5 == 2:
        Process8.q5 = " OUT OF SCOPE"
    if Process8.q6 == 0:
        Process8.q6 = "OK"
    if Process8.q6 == 1:
        Process8.q6 = " RED"
    if Process8.q6 == 2:
        Process8.q6 = " OUT OF SCOPE"
    if Process8.q7 == 0:
        Process8.q7 = "OK"
    if Process8.q7 == 1:
        Process8.q7 = " RED"
    if Process8.q7 == 2:
        Process8.q7 = " OUT OF SCOPE"
    if Process8.q8 == 0:
        Process8.q8 = "OK"
    if Process8.q8 == 1:
        Process8.q8 = " RED"
    if Process8.q8 == 2:
        Process8.q8 = " OUT OF SCOPE"
    if Process8.q9 == 0:
        Process8.q9 = "OK"
    if Process8.q9 == 1:
        Process8.q9 = " RED"
    if Process8.q9 == 2:
        Process8.q9 = " OUT OF SCOPE"
    if Process8.q10 == 0:
        Process8.q10 = "OK"
    if Process8.q10 == 1:
        Process8.q10 = " RED"
    if Process8.q10 == 2:
        Process8.q10 = " OUT OF SCOPE"
    if Process8.q11 == 0:
        Process8.q11 = "OK"
    if Process8.q11 == 1:
        Process8.q11 = " RED"
    if Process8.q11 == 2:
        Process8.q11 = " OUT OF SCOPE"
    if Process8.q12 == 0:
        Process8.q12 = "OK"
    if Process8.q12 == 1:
        Process8.q12 = " RED"
    if Process8.q12 == 2:
        Process8.q12 = " OUT OF SCOPE"
    if Process8.q13 == 0:
        Process8.q13 = "OK"
    if Process8.q13 == 1:
        Process8.q13 = " RED"
    if Process8.q13 == 2:
        Process8.q13 = "OUT OF SCOPE"
    if Process8.q14 == 0:
        Process8.q14 = "OK"
    if Process8.q14 == 1:
        Process8.q14 = " RED"
    if Process8.q14 == 2:
        Process8.q14 = " OUT OF SCOPE"

    if Process8_2.q1111 == 0:
        Process8_2.q1111 = "OK"
    if Process8_2.q1111 == 1:
        Process8_2.q1111 = "CONDITIONAL ADMISSION"    
    if Process8_2.q1111 == 2:
        Process8_2.q1111 = "RED"  

    if Process8_2.q3333 == 0:
        Process8_2.q3333 = "Aydin Kongel"
    if Process8_2.q3333 == 1:
        Process8_2.q3333 = "Ferdi Akdemir"    
    if Process8_2.q4444 == 0:
        Process8_2.q4444 = "Aydin Kongel"
    if Process8_2.q4444 == 1:
        Process8_2.q4444 = "Ferdi Akdemir"    

    date = Process8_2.created_on.date

    mapping = [('Ğ', 'G'), ('İ', 'I'),('Ş','s'), ('ı','i'), ('ğ','g'),('ş','s') ]
    for k, v in mapping:
        Process8.content = Process8.content.replace(k, v)
        montajname = montajname.replace(k, v)
        testname = testname.replace(k, v)
    if product:
        pdf, result = render_to_pdf(
            'pdf/adim8.html',
            {
                'tarih': date,
                'musteri': product.customer_order_no,
                'uretim_siparis_no':product.order_position_no,
                'ident': product.reference_no,
                'rno': product.imageno,
                'adet': product.quantity,
                'montajyapan': montajname,
                'testiyapan': testname,
                'temizlik': Process8.q1,
                'darbe': Process8.q2,
                'acik':Process8.q3,
                'eksik':Process8.q4,
                'hortum': Process8.q5,
                'boya': Process8.q6,
                'uyari': Process8.q7,
                'basinc': Process8.q8,
                'yag': Process8.q9,
                'dokumantasyon': Process8.q10,
                'kaldirma': Process8.q11,
                'unite': Process8.q12,
                'etiket': Process8.q13,
                'tank': Process8.q14,

                'aciklama': Process8.content,
                'karar': Process8_2.q1111,
                
                'kontrol': Process8_2.q3333,
                'onaylayan': Process8_2.q4444,
                'tarih1': date,
                'resim1':Process8.picture1,
                'resim2':Process8.picture2,
                'resim3':Process8.picture3,
                'resim4':Process8.picture4,
                'resim5':Process8.picture5,
                'resim6':Process8.picture6,
                'resim7':Process8.picture7,
                'resim8':Process8.picture8,
                'resim9':Process8.picture9,
                'resim10':Process8.picture10,
                
                'pass_smth': 'needed_in_render',
                'MEDIA_ROOT': settings.MEDIA_ROOT,
                'STATIC_ROOT': settings.STATICFILES_DIRS,
                'pagesize': 'A4',
            }

        )
        if not pdf.err:
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return HttpResponse('We had some errors')
    else:
        raise Http404


def pdf_sticker2(request, pk):
    product = get_object_or_404(Product, pk=pk)
    process7 = Process_7.objects.get(product__slug = product.slug)
    process7_2 = Process_7_2.objects.get(product__slug = product.slug)
    date = process7_2.created_on.date
   
    mapping = [('Ğ', 'G'), ('İ', 'I'),('Ş','s'), ('ı','i'), ('ğ','g'),('ş','s') ]
    for k, v in mapping:
        process7_2.q15 = process7_2.q15.replace(k, v)
        process7_2.q20 = process7_2.q20.replace(k, v)

    if process7_2.q6 == 0:
        process7_2.q6 = "Done"
    if process7_2.q6 == 1:
        process7_2.q6 = " Not Done"
    if process7_2.q7 == 0:
        process7_2.q7 = "Done"
    if process7_2.q7 == 1:
        process7_2.q7 = " Not Done"
    if process7_2.q8 == 0:
        process7_2.q8 = "Done"
    if process7_2.q8 == 1:
        process7_2.q8 = " Not Done"
    if process7_2.q9 == 0:
        process7_2.q9 = "Done"
    if process7_2.q9 == 1:
        process7_2.q9 = " Not Done"
    if process7_2.q10 == 0:
        process7_2.q10 = "Done"
    if process7_2.q10 == 1:
        process7_2.q10 = " Not Done"
    if process7_2.q11 == 0:
        process7_2.q11 = "Done"
    if process7_2.q11 == 1:
        process7_2.q11 = " Not Done"
    if process7_2.q12 == 0:
        process7_2.q12 = "Done"
    if process7_2.q12 == 1:
        process7_2.q12 = " Not Done"
    if process7_2.q13 == 0:
        process7_2.q13 = "Done"
    if process7_2.q13 == 1:
        process7_2.q13 = " Not Done"
    if process7_2.q14 == 0:
        process7_2.q14 = "Done"
    if process7_2.q14 == 1:
        process7_2.q14 = " Not Done"

    if process7_2.q1 == 0:
        process7_2.q1 = "Aydin Kongel"
    if process7_2.q1 == 1:
        process7_2.q1 = "Ferdi Akdemir"

    if process7_2.q2 == 0:
        process7_2.q2 = "Aydin Kongel"
    if process7_2.q2 == 1:
        process7_2.q2 = "Ferdi Akdemir"

    product.order_date = product.order_date.date
    if product:
        pdf, result = render_to_pdf(
            'pdf/adim7.html',
            {
                'sip': product.order_date,
                'siparis': product.order_position_no,
                'ident':product.reference_no ,
                'circuit':product.circuitno,

                'volume': product.volume,
                'pressur':product.working_pressure,
                'press':product.working_pressure,
                'adet': product.quantity,

                'montaj': process7_2.q6,
                'elek': process7_2.q7,
                'hortum': process7_2.q8,
                'fitting': process7_2.q9,
                'don': process7_2.q10,
                'func': process7_2.q11,
                'oil': process7_2.q12,
                'missing': process7_2.q13,
                'oilreservoir': process7_2.q14,

                'aciklama': process7_2.q15,

                'ral1': process7_2.q16,
                'ral2': process7_2.q17,
                'kal1': process7_2.q18,
                'kal2': process7_2.q19,

                '1pz':process7_2.q21,
                '1bar':process7_2.q37,
                '2pz':process7_2.q22,
                '2bar':process7_2.q38,
                '3pz':process7_2.q23,
                '3bar':process7_2.q39,
                '4pz':process7_2.q24,
                '4bar':process7_2.q40,
                '5pz':process7_2.q25,
                '5bar':process7_2.q41,
                '6pz':process7_2.q26,
                '6bar':process7_2.q42,
                '7pz':process7_2.q27,
                '7bar':process7_2.q43,
                '8pz':process7_2.q28,
                '8bar':process7_2.q44,
                '9pz':process7_2.q29,
                '9bar':process7_2.q45,
                '10pz':process7_2.q30,
                '10bar':process7_2.q46,
                '11pz':process7_2.q31,
                '11bar':process7_2.q47,
                '12pz':process7_2.q32,
                '12bar':process7_2.q48,
                '13pz':process7_2.q33,
                '13bar':process7_2.q49,
                '14pz':process7_2.q34,
                '14bar':process7_2.q50,
                '15pz':process7_2.q35,
                '15bar':process7_2.q51,
                '16pz':process7_2.q36,
                '16bar':process7_2.q52,

                'resim1':process7.p1,
                'resim2':process7.p2,
                'resim3':process7.p3,
                'resim4':process7.p4,

                'aciklama2':process7_2.q20,

                'testdate': date,
                'testedby': process7_2.q1,
                'control': process7_2.q2,

                'pass_smth': 'needed_in_render',
                'MEDIA_ROOT': settings.MEDIA_ROOT,
                'STATIC_ROOT': settings.STATICFILES_DIRS,
                'pagesize': 'A4',
            }
        )
        if not pdf.err:
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return HttpResponse('We had some errors')
    else:
        raise Http404

def pdf_sticker3(request, pk):
    product = get_object_or_404(Product, pk=pk)
    process1 = Process_1.objects.get(product__slug = product.slug)
    process1_2 = Process_1_2.objects.get(product__slug = product.slug)
    process1.created_on = process1.created_on.date

    mapping = [('Ğ', 'G'), ('İ', 'I'),('Ş','s'), ('ı','i'), ('ğ','g'),('ş','s') ]
    for k, v in mapping:
        process1.q19 = process1.q19.replace(k, v)

    if process1.q1 == 0:
        process1.q1 = "INCI MAKINA"
    if process1.q1 == 1:
        process1.q1 = "SECKIN TORNA"
    if process1.q1 == 2:
        process1.q1 = "MODCON"
    if process1.q1 == 3:
        process1.q1 = "TEKNIK CIZGI"

    if process1.q7 == 0:
        process1.q7 = "ST37"
    if process1.q7 == 1:
        process1.q7 = "ST52"
    if process1.q7 == 2:
        process1.q7 = "PASLANMAZ"
    if process1.q7 == 3:
        process1.q7 = "ALUMINYUM"

    if process1.q8 == 0:
        process1.q8 = "OK"
    if process1.q8 == 1:
        process1.q8 = "RED"
    if process1.q8 == 2:
        process1.q8 = "OUT OF SCOPE"

    if process1.q9 == 0:
        process1.q9 = "OK"
    if process1.q9 == 1:
        process1.q9 = "RED"
    if process1.q9 == 2:
        process1.q9 = "OUT OF SCOPE"    
    
    if process1.q10 == 0:
        process1.q10 = "OK"
    if process1.q10 == 1:
        process1.q10 = "RED"
    if process1.q10 == 2:
        process1.q10 = "OUT OF SCOPE"   

    if process1.q11 == 0:
        process1.q11 = "OK"
    if process1.q11 == 1:
        process1.q11 = "RED"
    if process1.q11 == 2:
        process1.q11 = "OUT OF SCOPE"

    if process1.q12 == 0:
        process1.q12 = "OK"
    if process1.q12 == 1:
        process1.q12 = "RED"
    if process1.q12 == 2:
        process1.q12 = "OUT OF SCOPE"

    if process1.q13 == 0:
        process1.q13 = "OK"
    if process1.q13 == 1:
        process1.q13 = "RED"
    if process1.q13 == 2:
        process1.q13 = "OUT OF SCOPE"

    if process1.q14 == 0:
        process1.q14 = "OK"
    if process1.q14 == 1:
        process1.q14 = "RED"
    if process1.q14 == 2:
        process1.q14 = "OUT OF SCOPE"

    if process1.q15 == 0:
        process1.q15 = "OK"
    if process1.q15 == 1:
        process1.q15 = "RED"
    if process1.q15 == 2:
        process1.q15 = "OUT OF SCOPE"

    if process1.q16 == 0:
        process1.q16 = "OK"
    if process1.q16 == 1:
        process1.q16 = "RED"
    if process1.q16 == 2:
        process1.q16 = "OUT OF SCOPE"

    if process1.q17 == 0:
        process1.q17 = "OK"
    if process1.q17 == 1:
        process1.q17 = "RED"
    if process1.q17 == 2:
        process1.q17 = "OUT OF SCOPE"

    if process1.q18 == 0:
        process1.q18 = "OK"
    if process1.q18 == 1:
        process1.q18 = "RED"
    if process1.q18 == 2:
        process1.q18 = "OUT OF SCOPE"

    if process1.q1111 == 0:
        process1.q1111 = "OK"
    if process1.q1111 == 1:
        process1.q1111 = "CONDITIONAL ADMISSION"
    if process1.q1111 == 2:
        process1.q1111 = "RED"

    if process1.q2222 == 0:
        process1.q2222 = "Rexroth"
    if process1.q2222 == 1:
        process1.q2222 = "Supplier"



    if product:
        pdf, result = render_to_pdf(
            'pdf/adim1.html',
            {
                'tarih':process1.created_on,
                'yansanayi':process1.q1,
                'ssiparis':product.customer_order_no,
                'usiparis':product.order_position_no,
                'ident':product.reference_no,
                'resimno':product.imageno,
                'adet':product.quantity,
                'tankturu':process1.q7,
                'eksen':process1.q8,
                'deformasyon':process1.q9,
                'taslama':process1.q10,
                'yuzey':process1.q11,
                'astar':process1.q12,
                'operasyon':process1.q13,
                'kaynak':process1.q14,
                'manson':process1.q15,
                'kaynakdikis':process1.q16,
                'tanktahliye':process1.q17,
                'paketleme':process1.q18,

                'resim1':process1.picture1,
                'resim2':process1.picture2,
                'resim3':process1.picture3,
                'resim4':process1.picture4,
                'resim5':process1.picture5,
                'resim6':process1.picture6,
                'resim7':process1.picture7,
                'resim8':process1.picture8,

                '1M': process1.q20,
                '1P1': process1.q21,
                '1P2': process1.q22,
                '1P3': process1.q23,
                '1P4': process1.q24,
                '1P5': process1.q25,
                '1P6': process1.q26,
                '1P7': process1.q27,
                '1P8': process1.q28,
                '1P9': process1.q29,
                '1P10': process1.q30,

                '2M': process1.q31,
                '2P1': process1.q32,
                '2P2': process1.q33,
                '2P3': process1.q34,
                '2P4': process1.q35,
                '2P5': process1.q36,
                '2P6': process1.q37,
                '2P7': process1.q38,
                '2P8': process1.q39,
                '2P9': process1.q40,
                '2P10': process1.q41,

                '3M': process1.q42,
                '3P1': process1.q43,
                '3P2': process1.q44,
                '3P3': process1.q45,
                '3P4': process1.q46,
                '3P5': process1.q47,
                '3P6': process1.q48,
                '3P7': process1.q49,
                '3P8': process1.q50,
                '3P9': process1.q51,
                '3P10': process1.q52,

                '4M': process1.q53,
                '4P1': process1.q54,
                '4P2': process1.q55,
                '4P3': process1.q56,
                '4P4': process1.q57,
                '4P5': process1.q58,
                '4P6': process1.q59,
                '4P7': process1.q60,
                '4P8': process1.q61,
                '4P9': process1.q62,
                '4P10': process1.q63,

                '5M': process1.q64,
                '5P1': process1.q65,
                '5P2': process1.q66,
                '5P3': process1.q67,
                '5P4': process1.q68,
                '5P5': process1.q69,
                '5P6': process1.q70,
                '5P7': process1.q71,
                '5P8': process1.q72,
                '5P9': process1.q73,
                '5P10': process1.q74,

                '6M': process1.q75,
                '6P1': process1.q76,
                '6P2': process1.q77,
                '6P3': process1.q78,
                '6P4': process1.q79,
                '6P5': process1.q80,
                '6P6': process1.q81,
                '6P7': process1.q82,
                '6P8': process1.q83,
                '6P9': process1.q84,
                '6P10': process1.q85,

                '7M': process1.q86,
                '7P1': process1.q87,
                '7P2': process1.q88,
                '7P3': process1.q89,
                '7P4': process1.q90,
                '7P5': process1.q91,
                '7P6': process1.q92,
                '7P7': process1.q93,
                '7P8': process1.q94,
                '7P9': process1.q95,
                '7P10': process1.q96,

                '8M': process1.q97,
                '8P1': process1.q98,
                '8P2': process1.q99,
                '8P3': process1.q100,
                '8P4': process1.q101,
                '8P5': process1.q102,
                '8P6': process1.q103,
                '8P7': process1.q104,
                '8P8': process1.q105,
                '8P9': process1.q106,
                '8P10': process1.q107,

                '9M': process1.q108,
                '9P1': process1.q109,
                '9P2': process1.q110,
                '9P3': process1.q111,
                '9P4': process1.q112,
                '9P5': process1.q113,
                '9P6': process1.q114,
                '9P7': process1.q115,
                '9P8': process1.q116,
                '9P9': process1.q117,
                '9P10': process1.q118,

                '10M': process1.q119,
                '10P1': process1.q120,
                '10P2': process1.q121,
                '10P3': process1.q122,
                '10P4': process1.q123,
                '10P5': process1.q124,
                '10P6': process1.q125,
                '10P7': process1.q126,
                '10P8': process1.q127,
                '10P9': process1.q128,
                '10P10': process1.q129,

                '11M': process1.q130,
                '11P1': process1.q131,
                '11P2': process1.q132,
                '11P3': process1.q133,
                '11P4': process1.q134,
                '11P5': process1.q135,
                '11P6': process1.q136,
                '11P7': process1.q137,
                '11P8': process1.q138,
                '11P9': process1.q139,
                '11P10': process1.q140,

                '12M': process1.q141,
                '12P1': process1.q142,
                '12P2': process1.q143,
                '12P3': process1.q144,
                '12P4': process1.q145,
                '12P5': process1.q146,
                '12P6': process1.q147,
                '12P7': process1.q148,
                '12P8': process1.q149,
                '12P9': process1.q150,
                '12P10': process1.q151,

                '13M': process1.q152,
                '13P1': process1.q153,
                '13P2': process1.q154,
                '13P3': process1.q155,
                '13P4': process1.q156,
                '13P5': process1.q157,
                '13P6': process1.q158,
                '13P7': process1.q159,
                '13P8': process1.q160,
                '13P9': process1.q161,
                '13P10': process1.q162,

                '14M': process1.q163,
                '14P1': process1.q164,
                '14P2': process1.q165,
                '14P3': process1.q166,
                '14P4': process1.q167,
                '14P5': process1.q168,
                '14P6': process1.q169,
                '14P7': process1.q170,
                '14P8': process1.q171,
                '14P9': process1.q172,
                '14P10': process1.q173,

                '15M': process1.q174,
                '15P1': process1.q175,
                '15P2': process1.q176,
                '15P3': process1.q177,
                '15P4': process1.q178,
                '15P5': process1.q179,
                '15P6': process1.q180,
                '15P7': process1.q181,
                '15P8': process1.q182,
                '15P9': process1.q183,
                '15P10': process1.q184,

                '16M': process1.q185,
                '16P1': process1.q186,
                '16P2': process1.q187,
                '16P3': process1.q188,
                '16P4': process1.q189,
                '16P5': process1.q190,
                '16P6': process1.q191,
                '16P7': process1.q192,
                '16P8': process1.q193,
                '16P9': process1.q194,
                '16P10': process1.q195,

                '17M': process1.q196,
                '17P1': process1.q197,
                '17P2': process1.q198,
                '17P3': process1.q199,
                '17P4': process1.q200,
                '17P5': process1.q201,
                '17P6': process1.q202,
                '17P7': process1.q203,
                '17P8': process1.q204,
                '17P9': process1.q205,
                '17P10': process1.q206,

                '18M': process1.q207,
                '18P1': process1.q208,
                '18P2': process1.q209,
                '18P3': process1.q210,
                '18P4': process1.q211,
                '18P5': process1.q212,
                '18P6': process1.q213,
                '18P7': process1.q214,
                '18P8': process1.q215,
                '18P9': process1.q216,
                '18P10': process1.q217,

                '19M': process1.q218,
                '19P1': process1.q219,
                '19P2': process1.q220,
                '19P3': process1.q221,
                '19P4': process1.q222,
                '19P5': process1.q223,
                '19P6': process1.q224,
                '19P7': process1.q225,
                '19P8': process1.q226,
                '19P9': process1.q227,
                '19P10': process1.q228,

                '20M': process1.q229,
                '20P1': process1.q230,
                '20P2': process1.q231,
                '20P3': process1.q232,
                '20P4': process1.q233,
                '20P5': process1.q234,
                '20P6': process1.q235,
                '20P7': process1.q236,
                '20P8': process1.q237,
                '20P9': process1.q238,
                '20P10': process1.q239,

                'remarks':process1.q19,

                'karar':process1.q1111,
                'ekislem':process1.q2222,
                'kontrol':process1.q3333,
                'onaylayan':process1_2.q4444,

                'pass_smth': 'needed_in_render',
                'MEDIA_ROOT': settings.MEDIA_ROOT,
                'STATIC_ROOT': settings.STATICFILES_DIRS,
                'pagesize': 'A4',
            }
        )
        if not pdf.err:
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return HttpResponse('We had some errors')
    else:
        raise Http404

from io import StringIO, BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(
        BytesIO(html.encode("utf-8")),
        dest=result,
        encoding="utf-8"
    )
    return pdf, result

##################pdf kütüphaneleri#####################
@login_required
def index(request):
    total_product = int(len(Product.objects.all()))
    if total_product == 0:
        controlled_product = 0
        under_control = 0
        production_rate = 0
    else:
        controlled_product = int(len(Process_8_2.objects.all()))
        under_control = int(total_product - controlled_product)
        production_rate = float(controlled_product * 100 /total_product )
        production_rate = round(production_rate, 1)

    context = {
        "total_product":total_product,
        "under_control":under_control,
        "production_rate":production_rate,
        "controlled_product": controlled_product,
    }
    return render(request, 'index.html', context=context)

import datetime
from datetime import timedelta
from django.http import JsonResponse

@login_required
def population_chart(request):
    labels = []
    data = []

    urunler = Product.objects.all().order_by('-created_on')[:10]
    suan = datetime.datetime.now().date()
    datetimeFormat = '%Y-%m-%d'

    for i in urunler:
        diff = datetime.datetime.strptime(str(suan), datetimeFormat) - datetime.datetime.strptime(str(i.created_on.date()), datetimeFormat)

        labels.append(i.slug)
        data.append(diff.days)
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


@login_required
def user_profile(request):

    context = {
        'title' : 'Process List',
    }

    return render(request, 'profile/profil.html', context=context)

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
        "name" : 'Product List',
    }

    return render(request, 'product/list_product.html', context=context)

class Created_by():
    def __init__(self,model,request, tip):
        self.obj = tip.objects.latest('pk')
        if self.obj.created_by is None:
            self.obj.created_by = request.user
        self.obj.updated_by = request.user
        self.obj.save()

@login_required
def created_updated(model, request):
    obj = Product.objects.latest('pk')
    if obj.created_by is None:
        obj.created_by = request.user
    obj.updated_by = request.user
    obj.save()

all_users = User.objects.all()

@login_required
def product_create(request):
    
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(data = request.POST)
        if form.is_valid():    
            form.save()
            cre_1 = Created_by(ProductForm, request, Product)
            #created_updated(ProductForm, request)
            return HttpResponseRedirect(reverse('list-product'))

    return render(request, 'product/create_product.html', context = {'form':form, 'all_users':all_users})


@login_required
def product_detail(request, pk):
    username = request.user.username
    p1 = None
    p2 = None
    p3 = None
    p4 = None
    p5 = None
    p6 = None
    p7 = None
    p8 = None
    product = get_object_or_404(Product, pk=pk)
    global urun
    global position_no
    position_no = product.order_position_no
    urun = get_object_or_404(Product, pk=pk)
    if urun == None:
        urun = ""
    #1.süreç
    if Process_1.objects.filter(product__slug = product.slug):
        if Process_1_2.objects.filter(product__slug = product.slug):
            process1 = Process_1.objects.get(product__slug = product.slug)
            deger_1 = 2 #ikisi de var
        else:
            process1 = Process_1.objects.get(product__slug = product.slug)
            deger_1 = 1
        p1 = process1.created_by
    else:
        process1 = ''
        deger_1 = 0 #start da finish de yok
    
    #2.süreç
    if Process_2.objects.filter(product__slug = product.slug):
        if Process_2_2.objects.filter(product__slug = product.slug):
            process2 = Process_2.objects.get(product__slug = product.slug)
            deger_2 = 2 #ikisi de var
        else:
            process2 = Process_2.objects.get(product__slug = product.slug)
            deger_2 = 1
        p2 = process2.created_by
    else:
        process2 = ''
        deger_2 = 0 #start da finish de yok

    #3.süreç
    if Process_3.objects.filter(product__slug = product.slug):
        if Process_3_2.objects.filter(product__slug = product.slug):
            process3 = Process_3.objects.get(product__slug = product.slug)
            deger_3 = 2 #ikisi de var
        else:
            process3 = Process_3.objects.get(product__slug = product.slug)
            deger_3 = 1
        p3 = process3.created_by

    else:
        process3 = ''
        deger_3 = 0 #start da finish de yok
    #4.süreç
    if Process_4.objects.filter(product__slug = product.slug):
        if Process_4_2.objects.filter(product__slug = product.slug):
            process4 = Process_4.objects.get(product__slug = product.slug)
            deger_4 = 2 #ikisi de var
        else:
            process4 = Process_4.objects.get(product__slug = product.slug)
            deger_4 = 1
        p4 = process4.created_by

    else:
        process4 = ''
        deger_4 = 0 #start da finish de yok
    #5.süreç
    if Process_5.objects.filter(product__slug = product.slug):
        if Process_5_2.objects.filter(product__slug = product.slug):
            process5 = Process_5.objects.get(product__slug = product.slug)
            deger_5 = 2 #ikisi de var
        else:
            process5 = Process_5.objects.get(product__slug = product.slug)
            deger_5 = 1
        p5 = process5.created_by

    else:
        process5 = ''
        deger_5 = 0 #start da finish de yok
    #6.süreç
    if Process_6.objects.filter(product__slug = product.slug):
        if Process_6_2.objects.filter(product__slug = product.slug):
            process6 = Process_6.objects.get(product__slug = product.slug)
            deger_6 = 2 #ikisi de var
        else:
            process6 = Process_6.objects.get(product__slug = product.slug)
            deger_6 = 1
        p6 = process6.created_by

    else:
        process6 = ''
        deger_6 = 0 #start da finish de yok
    #7.süreç
    if Process_7.objects.filter(product__slug = product.slug):
        if Process_7_2.objects.filter(product__slug = product.slug):
            process7 = Process_7.objects.get(product__slug = product.slug)
            deger_7 = 2 #ikisi de var
        else:
            process7 = Process_7.objects.get(product__slug = product.slug)
            deger_7 = 1
        p7 = process7.created_by

    else:
        process7 = ''
        deger_7 = 0 #start da finish de yok
    #8.süreç
    if Process_8.objects.filter(product__slug = product.slug):
        if Process_8_2.objects.filter(product__slug = product.slug):
            process8 = Process_8.objects.get(product__slug = product.slug)
            deger_8 = 2 #ikisi de var
        else:
            process8 = Process_8.objects.get(product__slug = product.slug)
            deger_8 = 1
        p8 = process8.created_by
    else:
        process8 = ''
        deger_8 = 0 #start da finish de yok

    if str(p1) == str(username):
        p1 = 1
    if str(p2) == str(username):
        p2 = 1
    if str(p3) == str(username):
        p3 = 1
    if str(p4) == str(username):
        p4 = 1
    if str(p5) == str(username):
        p5 = 1
    if str(p6) == str(username):
        p6 = 1
    if str(p7) == str(username):
        p7 = 1
    if str(p8) == str(username):
        p8 = 1

    context = {
        'username':username,
        'p1':p1,
        'p2':p2,
        'p3':p3,
        'p4':p4,
        'p5':p5,
        'p6':p6,
        'p7':p7,
        'p8':p8,
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
def product_info(request, pk):
    
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=product, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-product'))

    context = {
        'product' : product,
        'form' : form,
    }

    return render(request, 'product/info_product.html', context=context)

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
    form = Process1Form(initial={'product': urun})
    if request.method == 'POST':
        form = Process1Form(data = request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            cre_1_1 = Created_by(Process1Form, request, Process_1)
            return HttpResponseRedirect(reverse('list-process1'))
    return render(request, 'process1/create_process.html', context = {'form':form, 'text':'Create New Process'})

@login_required
def process1_detail(request, pk):
    process = get_object_or_404(Process_1, pk=pk)
    product = Product.objects.get(slug = process.product)
    context = {
        'process' : process,
        'product' : product,
    }
    return render(request, 'process1/detail_process.html', context = context )

@login_required
def process1_update(request, pk):
    process = get_object_or_404(Process_1, pk=pk)
    form = Process1Form(instance=process, data=request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process1'))
    context = {
        'process' : process,
        'form' : form,
    }
    return render(request, 'process1/update_process.html', context=context)

@login_required
def process1_info(request, pk):
    process = get_object_or_404(Process_1, pk=pk)
    form = Process1Form(instance=process, data=request.POST or None)
    form2 = Process1_2Form(instance=process, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process1'))
    context = {
        'process' : process,
        'form' : form,
        'form2':form2,

    }
    return render(request, 'process1/info_process.html', context=context)

@login_required
def process1_delete(request, pk):
    process = get_object_or_404(Process_1, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process1'))

@login_required

def process1_list(request):
    names = []
    created_by = []
    created_on = []
    finished_on = []
    
    for i in Process_1.objects.all():
        for j in Process_1_2.objects.all():
            if i.product == j.product:
                names.append(j.product)
                created_by.append(j.created_by)
                created_on.append(i.created_on)
                finished_on.append(j.created_on)

    data = zip(names, created_by,created_on,finished_on)

    context = {
        'title' : 'Process 1 List',
        'data': data,
    }

    return render(request, 'process1/list_process.html', context=context)
    


#------ Process1_2 ------# 

create_1 = 'Ön Montaj Süreci Oluştur'
create_2 = ''
create_3 = ''

@login_required
def process1_2_create(request):
    form = Process1_2Form(initial={'product': urun})

    if request.method == 'POST':
        form = Process1_2Form(data = request.POST)
        if form.is_valid():
            form.save()
            cre_1_2 = Created_by(Process1_2Form, request, Process_1_2)
            return HttpResponseRedirect(reverse('list-process1'))

    return render(request, 'process1_2/create_process.html', context = {'form':form, 'text':'- Complete Process 1'})

@login_required
def process1_2_detail(request, pk):

    process = get_object_or_404(Process_1_2, pk=pk)
    product = Product.objects.get(slug = process.product)

    context = {
        'process' : process,
        'product' : product,

    }

    return render(request, 'process1_2/detail_process.html', context = context )

@login_required
def process1_2_update(request, pk):
    process = get_object_or_404(Process_1_2, pk=pk)
    form = Process1_2Form(instance=process, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process1_2'))


    context = {
        'process' : process,
        'form' : form,
    }

    return render(request, 'process1_2/update_process.html', context=context)

@login_required
def process1_2_delete(request, pk):
    process = get_object_or_404(Process_1_2, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process1_2'))

@login_required
def process1_2_list(request):

    context = {
        'title' : 'Process 1 List',
        "all_processes" : Process_1_2.objects.all(),

    }

    return render(request, 'process1/list_process.html', context=context)

#------ Process2 ------# 

@login_required
def process2_create(request):
    form = Process2Form(initial={'product': urun})

    if request.method == 'POST':
        form = Process2Form(data = request.POST)
        if form.is_valid():
            form.save()
            cre_2_1 = Created_by(Process2Form, request, Process_2)
            return HttpResponseRedirect(reverse('list-process2'))

    return render(request, 'process2/create_process.html', context = {'form':form})


@login_required
def process2_detail(request, pk):
    process = get_object_or_404(Process_2, pk=pk)
    product = Product.objects.get(slug = process.product)

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
def process2_info(request, pk):
    process = get_object_or_404(Process_2, pk=pk)
    form = Process2Form(instance=process, data=request.POST or None)
    form2 = Process2_2Form(instance=process, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process2'))

    context = {
        'process' : process,
        'form' : form,
        'form2': form2,
    }

    return render(request, 'process2/info_process.html', context=context)

@login_required
def process2_delete(request, pk):
    process = get_object_or_404(Process_2, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process2'))

@login_required
def process2_list(request):

    names = []
    created_by = []
    created_on = []
    finished_on = []
    
    for i in Process_2.objects.all():
        for j in Process_2_2.objects.all():
            if i.product == j.product:
                names.append(j.product)
                created_by.append(j.created_by)
                created_on.append(i.created_on)
                finished_on.append(j.created_on)

    data = zip(names, created_by,created_on,finished_on)

    context = {
        'title' : 'Process 2 List',
        'data': data,
    }

    return render(request, 'process2/list_process.html', context=context)

#------ Process2 ------# 

@login_required
def process2_2_create(request):
    form = Process2_2Form(initial={'product': urun})

    if request.method == 'POST':
        form = Process2_2Form(data = request.POST)
        if form.is_valid():
            form.save()
            cre_2_2 = Created_by(Process2_2Form, request, Process_2_2)
            return HttpResponseRedirect(reverse('list-process2'))

    return render(request, 'process2_2/create_process.html', context = {'form':form, 'text':'- Complete Process 2'})


@login_required
def process2_2_detail(request, pk):
    process = get_object_or_404(Process_2_2, pk=pk)
    product = Product.objects.get(slug = process.product)

    context = {
        'process' : process,
        'product' : product,

    }

    return render(request, 'process2_2/detail_process.html', context = context )

@login_required
def process2_2_update(request, pk):
    process = get_object_or_404(Process_2_2, pk=pk)
    form = Process2_2Form(instance=process, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process2_2'))


    context = {
        'process' : process,
        'form' : form,
    }

    return render(request, 'process2_2/update_process.html', context=context)

@login_required
def process2_2_delete(request, pk):
    process = get_object_or_404(Process_2_2, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process2_2'))

@login_required
def process2_2_list(request):
    context = {
        'title' : 'Process 2 List',
        "all_processes" : Process_2_2.objects.all(),

    }
    return render(request, 'process2/list_process.html', context=context)

#------ Process3 ------# 

@login_required
def process3_create(request):
    form = Process3Form(initial={'product': urun})

    if request.method == 'POST':
        form = Process3Form(data = request.POST)
        if form.is_valid():
            form.save()
            cre_3_1 = Created_by(Process3Form, request, Process_3)

            return HttpResponseRedirect(reverse('list-process3'))

    return render(request, 'process3/create_process.html', context = {'form':form})

@login_required
def process3_detail(request, pk):
    process = get_object_or_404(Process_3, pk=pk)
    product = Product.objects.get(slug = process.product)


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
def process3_info(request, pk):
    process = get_object_or_404(Process_3, pk=pk)
    form = Process3Form(instance=process, data=request.POST or None)
    form2 = Process3_2Form(instance=process, data=request.POST or None)

    if form.is_valid() and form2.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process3'))

    context = {
        'process' : process,
        'form' : form,
        'form2' : form2,
    }

    return render(request, 'process3/info_process.html', context=context)

@login_required
def process3_delete(request, pk):
    process = get_object_or_404(Process_3, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process3'))

@login_required
def process3_list(request):
    names = []
    created_by = []
    created_on = []
    finished_on = []
    
    for i in Process_3.objects.all():
        for j in Process_3_2.objects.all():
            if i.product == j.product:
                names.append(j.product)
                created_by.append(j.created_by)
                created_on.append(i.created_on)
                finished_on.append(j.created_on)

    data = zip(names, created_by,created_on,finished_on)

    context = {
        'title' : 'Process 3 List',
        'data': data,
    }

    return render(request, 'process3/list_process.html', context=context)




#------ Process3_2 ------# 

@login_required
def process3_2_create(request):
    form = Process3_2Form(initial={'product': urun})

    if request.method == 'POST':
        form = Process3_2Form(data = request.POST)
        if form.is_valid():
            form.save()
            cre_3_2 = Created_by(Process3_2Form, request, Process_3_2)
            
            return HttpResponseRedirect(reverse('list-process3'))

    return render(request, 'process3_2/create_process.html', context = {'form':form, 'text':'- Complete Process 3'})

@login_required
def process3_2_detail(request, pk):
    process = get_object_or_404(Process_3_2, pk=pk)
    product = Product.objects.get(slug = process.product)


    context = {
        'process' : process,
        'product' : product,

    }

    return render(request, 'process3_2/detail_process.html', context = context )

@login_required
def process3_2_update(request, pk):
    process = get_object_or_404(Process_3_2, pk=pk)
    form = Process3_2Form(instance=process, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process3'))


    context = {
        'process' : process,
        'form' : form,
    }

    return render(request, 'process3_2/update_process.html', context=context)

@login_required
def process3_2_delete(request, pk):
    process = get_object_or_404(Process_3_2, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process3_2'))

@login_required
def process3_2_list(request):
    context = {
        'title' : 'Process 3 List',
        "all_processes" : Process_3.objects.all(),

    }

    return render(request, 'process3/list_process.html', context=context)

#------ Process4 ------# 

@login_required
def process4_create(request):
    form = Process4Form(initial={'product': urun})

    if request.method == 'POST':
        form = Process4Form(data = request.POST)
        if form.is_valid():
            form.save()
            cre_4_1 = Created_by(Process4Form, request, Process_4)
            return HttpResponseRedirect(reverse('list-process4'))

    return render(request, 'process4/create_process.html', context = {'form':form})

@login_required
def process4_detail(request, pk):
    process = get_object_or_404(Process_4, pk=pk)
    product = Product.objects.get(slug = process.product)


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
def process4_info(request, pk):
    process = get_object_or_404(Process_4, pk=pk)
    form = Process4Form(instance=process, data=request.POST or None)
    form2 = Process4_2Form(instance=process, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process4'))


    context = {
        'process' : process,
        'form' : form,
        'form2': form2,
    }

    return render(request, 'process4/info_process.html', context=context)

@login_required
def process4_delete(request, pk):
    process = get_object_or_404(Process_4, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process4'))

@login_required
def process4_list(request):
    names = []
    created_by = []
    created_on = []
    finished_on = []
    
    for i in Process_4.objects.all():
        for j in Process_4_2.objects.all():
            if i.product == j.product:
                names.append(j.product)
                created_by.append(j.created_by)
                created_on.append(i.created_on)
                finished_on.append(j.created_on)

    data = zip(names, created_by,created_on,finished_on)

    context = {
        'title' : 'Process 4 List',
        'data': data,
    }

    return render(request, 'process4/list_process.html', context=context)





#------ Process4_2 ------# 

@login_required
def process4_2_create(request):
    form = Process4_2Form(initial={'product': urun})

    if request.method == 'POST':
        form = Process4_2Form(data = request.POST)
        if form.is_valid():
            form.save()
            cre_4_2 = Created_by(Process4_2Form, request, Process_4_2)
            return HttpResponseRedirect(reverse('list-process4'))

    return render(request, 'process4/create_process.html', context = {'form':form, 'text':'- Complete Process 4'})

@login_required
def process4_2_detail(request, pk):
    process = get_object_or_404(Process_4_2, pk=pk)
    product = Product.objects.get(slug = process.product)


    context = {
        'process' : process,
        'product' : product,

    }

    return render(request, 'process4_2/detail_process.html', context = context )

@login_required
def process4_2_update(request, pk):
    process = get_object_or_404(Process_4_2, pk=pk)
    form = Process4_2Form(instance=process, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process4'))


    context = {
        'process' : process,
        'form' : form,
    }

    return render(request, 'process4_2/update_process.html', context=context)

@login_required
def process4_2_delete(request, pk):
    process = get_object_or_404(Process_4_2, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process4_2'))

@login_required
def process4_2_list(request):
    context = {
        'title' : 'Process 4 List',
        "all_processes" : Process_4_2.objects.all(),

    }

    return render(request, 'process4/list_process.html', context=context)



#------ Process5 ------# 

@login_required
def process5_create(request):
    form = Process5Form(initial={'product': urun})

    if request.method == 'POST':
        form = Process5Form(data = request.POST)
        if form.is_valid():
            form.save()
            cre_5_1 = Created_by(Process5Form, request, Process_5)
            return HttpResponseRedirect(reverse('list-process5'))

    return render(request, 'process5/create_process.html', context = {'form':form})

@login_required
def process5_detail(request, pk):
    process = get_object_or_404(Process_5, pk=pk)
    product = Product.objects.get(slug = process.product)


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
def process5_info(request, pk):
    process = get_object_or_404(Process_5, pk=pk)
    form = Process5Form(instance=process, data=request.POST or None)
    form2 = Process5_2Form(instance=process, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process5'))


    context = {
        'process' : process,
        'form' : form,
        'form2':form2,
    }

    return render(request, 'process5/info_process.html', context=context)

@login_required
def process5_delete(request, pk):
    process = get_object_or_404(Process_5, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process5'))

@login_required
def process5_list(request):

    names = []
    created_by = []
    created_on = []
    finished_on = []
    
    for i in Process_5.objects.all():
        for j in Process_5_2.objects.all():
            if i.product == j.product:
                names.append(j.product)
                created_by.append(j.created_by)
                created_on.append(i.created_on)
                finished_on.append(j.created_on)

    data = zip(names, created_by,created_on,finished_on)

    context = {
        'title' : 'Process 5 List',
        'data': data,
    }

    return render(request, 'process5/list_process.html', context=context)

#------ Process5_2 ------# 

@login_required
def process5_2_create(request):
    form = Process5_2Form(initial={'product': urun})

    if request.method == 'POST':
        form = Process5_2Form(data = request.POST)
        if form.is_valid():
            form.save()
            cre_5_2 = Created_by(Process5_2Form, request, Process_5_2)
            return HttpResponseRedirect(reverse('list-process5'))

    return render(request, 'process5/create_process.html', context = {'form':form, 'text':'- Complete Process 5'})

@login_required
def process5_2_detail(request, pk):
    process = get_object_or_404(Process_5_2, pk=pk)
    product = Product.objects.get(slug = process.product)


    context = {
        'process' : process,
        'product' : product,

    }

    return render(request, 'process5_2/detail_process.html', context = context )

@login_required
def process5_2_update(request, pk):
    process = get_object_or_404(Process_5_2, pk=pk)
    form = Process5_2Form(instance=process, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process5_2'))


    context = {
        'process' : process,
        'form' : form,
    }

    return render(request, 'process5_2/update_process.html', context=context)

@login_required
def process5_2_delete(request, pk):
    process = get_object_or_404(Process_5_2, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process5_2'))

@login_required
def process5_2_list(request):
    context = {
        'title' : 'Process 5 List',
        "all_processes" : Process_5_2.objects.all(),

    }

    return render(request, 'process5/list_process.html', context=context)

#------ Process6 ------# 

@login_required
def process6_create(request):
    form = Process6Form(initial={'product': urun})

    if request.method == 'POST':
        form = Process6Form(data = request.POST)
        if form.is_valid():
            form.save()
            cre_6_1 = Created_by(Process6Form, request, Process_6)
            return HttpResponseRedirect(reverse('list-process6'))

    return render(request, 'process6/create_process.html', context = {'form':form})

@login_required
def process6_detail(request, pk):
    process = get_object_or_404(Process_6, pk=pk)
    product = Product.objects.get(slug = process.product)


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
def process6_info(request, pk):
    process = get_object_or_404(Process_6, pk=pk)
    form = Process6Form(instance=process, data=request.POST or None)
    form2 = Process6_2Form(instance=process, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process6'))


    context = {
        'process' : process,
        'form' : form,
        'form2': form2,
    }

    return render(request, 'process6/info_process.html', context=context)

@login_required
def process6_delete(request, pk):
    process = get_object_or_404(Process_6, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process6'))

@login_required
def process6_list(request):
    names = []
    created_by = []
    created_on = []
    finished_on = []
    
    for i in Process_6.objects.all():
        for j in Process_6_2.objects.all():
            if i.product == j.product:
                names.append(j.product)
                created_by.append(j.created_by)
                created_on.append(i.created_on)
                finished_on.append(j.created_on)

    data = zip(names, created_by,created_on,finished_on)

    context = {
        'title' : 'Process 6 List',
        'data': data,
    }

    return render(request, 'process6/list_process.html', context=context)

#------ Process6_2 ------# 

@login_required
def process6_2_create(request):
    form = Process6_2Form(initial={'product': urun})

    if request.method == 'POST':
        form = Process6_2Form(data = request.POST)
        if form.is_valid():
            form.save()
            cre_6_2 = Created_by(Process6_2Form, request, Process_6_2)
            return HttpResponseRedirect(reverse('list-process6'))

    return render(request, 'process6_2/create_process.html', context = {'form':form, 'text':'- Complete Process 6'})

@login_required
def process6_2_detail(request, pk):
    process = get_object_or_404(Process_6_2, pk=pk)
    product = Product.objects.get(slug = process.product)


    context = {
        'process' : process,
        'product' : product,

    }

    return render(request, 'process6_2/detail_process.html', context = context )

@login_required
def process6_2_update(request, pk):
    process = get_object_or_404(Process_6_2, pk=pk)
    form = Process6_2Form(instance=process, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process6_2'))


    context = {
        'process' : process,
        'form' : form,
    }

    return render(request, 'process6_2/update_process.html', context=context)

@login_required
def process6_2_delete(request, pk):
    process = get_object_or_404(Process_6_2, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process6_2'))

@login_required
def process6_2_list(request):
    context = {
        'title' : 'Process 6 List',
        "all_processes" : Process_6_2.objects.all(),

    }

    return render(request, 'process6/list_process.html', context=context)


#------ Process7 ------# 

@login_required
def process7_create(request):
    form = Process7Form(initial={'product': urun})

    if request.method == 'POST':
        form = Process7Form(data = request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            cre_7_1 = Created_by(Process7Form, request, Process_7)
            return HttpResponseRedirect(reverse('list-process7'))
        else: 
            form = Process8Form() 
    return render(request, 'process7/create_process.html', context = {'form':form})

@login_required
def process7_detail(request, pk):
    process = get_object_or_404(Process_7, pk=pk)
    product = Product.objects.get(slug = process.product)


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
def process7_info(request, pk):
    process = get_object_or_404(Process_7, pk=pk)
    form = Process7Form(instance=process, data=request.POST or None)
    form2 = Process7_2Form(instance=process, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process7'))


    context = {
        'process' : process,
        'form' : form,
        'form2': form2,
    }

    return render(request, 'process7/info_process.html', context=context)

@login_required
def process7_delete(request, pk):
    process = get_object_or_404(Process_7, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process7'))

@login_required
def process7_list(request):
    names = []
    created_by = []
    created_on = []
    finished_on = []
    
    for i in Process_7.objects.all():
        for j in Process_7_2.objects.all():
            if i.product == j.product:
                names.append(j.product)
                created_by.append(j.created_by)
                created_on.append(i.created_on)
                finished_on.append(j.created_on)

    data = zip(names, created_by,created_on,finished_on)

    context = {
        'title' : 'Process 7 List',
        'data': data,
    }

    return render(request, 'process7/list_process.html', context=context)
#------ Process7_2 ------# 

@login_required
def process7_2_create(request):
    form = Process7_2Form(initial={'product': urun})
    if request.method == 'POST':
        form = Process7_2Form(data = request.POST)
        if form.is_valid():
            form.save()
            
            cre_7_2 = Created_by(Process7_2Form, request, Process_7_2)
            return HttpResponseRedirect(reverse('list-process7'))

    return render(request, 'process7_2/create_process.html', context = {'form':form, 'text':'- Complete Process 7'})

@login_required
def process7_2_detail(request, pk):
    process = get_object_or_404(Process_7_2, pk=pk)
    product = Product.objects.get(slug = process.product)


    context = {
        'process' : process,
        'product' : product,

    }

    return render(request, 'process7_2/detail_process.html', context = context )

@login_required
def process7_2_update(request, pk):
    process = get_object_or_404(Process_7_2, pk=pk)
    form = Process7_2Form(instance=process, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process7_2'))


    context = {
        'process' : process,
        'form' : form,
    }

    return render(request, 'process7_2/update_process.html', context=context)

@login_required
def process7_2_delete(request, pk):
    process = get_object_or_404(Process_7_2, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process7_2'))

@login_required
def process7_2_list(request):
    context = {
        'title' : 'Process 7 List',
        "all_processes" : Process_7_2.objects.all(),

    }

    return render(request, 'process7/list_process.html', context=context)

#------ Process8 ------# 

@login_required
def process8_create(request):
    form = Process8Form(initial={'product': urun})

    if request.method == 'POST':
        form = Process8Form(data = request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            cre_8_1 = Created_by(Process8Form, request, Process_8)
            return HttpResponseRedirect(reverse('list-process8'))
        else: 
            form = Process8Form() 
    return render(request, 'process8/create_process.html', context = {'form':form})

@login_required
def process8_detail(request, pk):
    process = get_object_or_404(Process_8, pk=pk)
    product = Product.objects.get(slug = process.product)

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
def process8_info(request, pk):
    process = get_object_or_404(Process_8, pk=pk)
    form = Process8Form(instance=process, data=request.POST or None)
    form2 = Process8_2Form(instance=process, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process8'))


    context = {
        'process' : process,
        'form' : form,
        'form2': form2,
    }

    return render(request, 'process8/info_process.html', context=context)

@login_required
def process8_delete(request, pk):
    process = get_object_or_404(Process_8, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process8'))

@login_required
def process8_list(request):
    names = []
    created_by = []
    created_on = []
    finished_on = []
    
    for i in Process_8.objects.all():
        for j in Process_8_2.objects.all():
            if i.product == j.product:
                names.append(j.product)
                created_by.append(j.created_by)
                created_on.append(i.created_on)
                finished_on.append(j.created_on)

    data = zip(names, created_by,created_on,finished_on)

    context = {
        'title' : 'Process 8 List',
        'data': data,
    }

    return render(request, 'process8/list_process.html', context=context)

    #------ Process8_2 ------# 

@login_required
def process8_2_create(request):
    form = Process8_2Form(initial={'product': urun})

    if request.method == 'POST':
        form = Process8_2Form(data = request.POST)
        if form.is_valid():
            form.save()
            cre_8_2 = Created_by(Process8_2Form, request, Process_8_2)
            return HttpResponseRedirect(reverse('list-process8'))

    return render(request, 'process8_2/create_process.html', context = {'form':form, 'text':'- Complete Process 1'})

@login_required
def process8_2_detail(request, pk):
    process = get_object_or_404(Process_8_2, pk=pk)
    product = Product.objects.get(slug = process.product)

    context = {
        'process' : process,
        'product' : product,

    }

    return render(request, 'process8_2/detail_process.html', context = context )

@login_required
def process8_2_update(request, pk):
    process = get_object_or_404(Process_8_2, pk=pk)
    form = Process8Form(instance=process, data=request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list-process8_2'))


    context = {
        'process' : process,
        'form' : form,
    }

    return render(request, 'process8_2/update_process.html', context=context)

@login_required
def process8_2_delete(request, pk):
    process = get_object_or_404(Process_8_2, pk=pk)
    process.delete()
    return HttpResponseRedirect(reverse('list-process8_2'))

@login_required
def process8_2_list(request):
    context = {
        'title' : 'Process 8 List',
        "all_processes" : Process_8_2.objects.all(),

    }

    return render(request, 'process8/list_process.html', context=context)




    