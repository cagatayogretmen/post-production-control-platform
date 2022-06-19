from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.timezone import now
from django.conf import settings
from django.utils.text import slugify
import datetime
from datetime import timedelta
from multiselectfield import MultiSelectField

Multiple = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
    (11, '11'),
    (12, '12'),
    (13, '13'),
    (14, '14')
)
RESULT = (
    (0, 'Yes'),
    (1, 'No'),
    (2, 'Not Relavant')
)
YRESULT = (
    (0, 'INCI MAKINA'),
    (1, 'SECKIN TORNA'),
    (2, 'MODCON'),
    (3, "TEKNIK CIZGI")
)

TRESULT = (
    (0, 'ST37/ S235'),
    (1, 'ST52/ S355'),
    (2, 'Stainless Steel'),
    (3, 'Aluminium')
)

KRESULT = (
    (0, 'OK'),
    (1, 'Conditionally Approved'),
    (2, 'RED')
)

KKRESULT = (
    (0, 'OK'),
    (1, 'N.OK'),
    (2, 'Not Applicable')
)

KKARESULT = (
    (0, 'OK'),
    (1, 'N.OK'),
    (2, 'Not Applicable')

)

ERESULT = (
    (2, '.......'),
    (0, 'Rexroth'),
    (1, 'Supplier'),

)

KORESULT = (
    (0, 'Aydın Kongel'),
    (1, 'Ferdi Akdemir'),
)

ARESULT = (
    (0, 'DONE'),
    (1, 'Not Done')
)

BRESULT = (
    (0, 'None'),
    (1, 'Detected')
)

CRESULT = (
    (0, 'Yes'),
    (1, 'No')
)

SRESULT = (
    (0, 'Rexroth'),
    (1, 'Not Tested')
)

YYRESULT = (
    (0, 'None'),
    (1, 'Dedected')
)


sorular = ['soru1','soru2','soru3','soru4','soru5']


class Product(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    #product_name = models.CharField(max_length=200, verbose_name='Product Name', unique=False)
    customer_order_no = models.IntegerField(unique=False, blank=False, verbose_name='Customer Order No: ')
    order_position_no = models.IntegerField(unique=False, blank=False, verbose_name='Order Position No: ')
    reference_no = models.CharField(default="R", max_length=200, blank=True,verbose_name='Reference No:')
    circuitno = models.IntegerField(default=0, unique=False, blank=True, verbose_name = 'Hydraulic Circuit No:')
    tank_reference_no = models.CharField(default=0, unique=False, blank=True,max_length=200, verbose_name='Oil Tank Ref. No:')
    imageno = models.CharField(default=0, max_length=200, unique=False, blank=True,verbose_name = 'Oil Tank Drawing No:')  
    volume = models.IntegerField(default=0, unique=False, blank=True, verbose_name = 'Oil Tank Volume(lt):')
    quantity = models.IntegerField(default=0, unique=False, blank=True, verbose_name='Quantity:')
    stand_ref_no = models.IntegerField(default=0, unique=False, blank=True, verbose_name='Accu Stand Ref. No:')
    stand_drawing_no = models.IntegerField(default=0, unique=False, blank=True, verbose_name='Accu Stand Drawing No:')
    valve_stand_ref_no = models.IntegerField(default=0, unique=False, blank=True, verbose_name='Valve Stand No:')
    valve_stand_drawing_no = models.IntegerField(default=0, unique=False, blank=True, verbose_name='Valve Stand Drawing No:')
    working_pressure = models.IntegerField(default=0, unique=False, blank=True, verbose_name='System Working Pressure (Bar):')
    test_pressure = models.IntegerField(default=0, unique=False, blank=True, verbose_name='System Test Pressure (Bar):')
    order_date = models.DateTimeField(default =datetime.date.today,unique=False, blank=True, verbose_name='Order Date ')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL )   
    slug = models.SlugField(unique=True)
    updated_on = models.DateTimeField(auto_now= True)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    def save(self, *args, **kwargs):
        self.slug = slugify(" {} / {} ".format(self.customer_order_no, self.order_position_no))
        super(Product, self).save(*args, **kwargs)
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.slug

def Process1_image(instance, filename): 
    return 'Product_Pictures/{0}/Process1/{1}'.format(instance.product, filename)

class Process_1(models.Model): #giriş kalite kontrol
    product = models.ForeignKey(Product, on_delete= models.CASCADE,related_name='product_process1', verbose_name = 'Product Name')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL )   
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    q0 = models.IntegerField(default=0, unique=False, blank=True, verbose_name='P.O. No:')
    q1 = models.CharField(max_length=200,blank=False, verbose_name='Supplier')
    q2 = models.CharField(default="",max_length=200,blank=False, verbose_name='Stainless Steel/Aluminium Quality')
    q7 = models.IntegerField(choices=TRESULT,  blank=False, verbose_name='Tank Material')
    q8 = models.IntegerField(choices=KKARESULT,  blank=False, verbose_name='Axial Deviation')
    q9 = models.IntegerField(choices=KKRESULT,  blank=False, verbose_name='Deformation on Surface')
    q10 = models.IntegerField(choices=KKRESULT,  blank=False, verbose_name='Grinding Scratches and Paste Used')
    q11 = models.IntegerField(choices=KKRESULT,  blank=False, verbose_name='Cleanliness')
    q12 = models.IntegerField(default=0, blank=False, verbose_name='Primary Coating Thickness (µ)')
    q13 = models.IntegerField(choices=KKRESULT,  blank=False, verbose_name='Missing of Operation')
    q14 = models.IntegerField(choices=KKRESULT,  blank=False, verbose_name='Welding Quality')
    q15 = models.IntegerField(choices=KKRESULT,  blank=False, verbose_name='MAG Welding Start Finish Point Check')
    q16 = models.IntegerField(choices=KKRESULT,  blank=False, verbose_name='Stainless Tank Passivation Check')
    q17 = models.IntegerField(choices=KKRESULT,  blank=False, verbose_name='Aluminium Tank Drain Hole Crack Chck')
    q18 = models.IntegerField(choices=KKRESULT,  blank=False, verbose_name='Packaging')

    picture1 = models.ImageField(upload_to= Process1_image, blank=True, null=True, verbose_name='Upload Image 1')
    picture2 = models.ImageField(upload_to=Process1_image, blank=True, null=True, verbose_name='Upload Image 2')
    picture3 = models.ImageField(upload_to=Process1_image, blank=True, null=True, verbose_name='Upload Image 3')
    picture4 = models.ImageField(upload_to=Process1_image, blank=True, null=True, verbose_name='Upload Image 4')
    picture5 = models.ImageField(upload_to=Process1_image, blank=True, null=True, verbose_name='Upload Image 5')
    picture6 = models.ImageField(upload_to=Process1_image, blank=True, null=True, verbose_name='Upload Image 6')
    picture7 = models.ImageField(upload_to=Process1_image, blank=True, null=True, verbose_name='Upload Image 7')
    picture8 = models.ImageField(upload_to=Process1_image, blank=True, null=True, verbose_name='Upload Image 8')
    
    q20 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='1M')
    q21 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='1P1')
    q22 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='1P2')
    q23 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='1P3')
    q24 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='1P4')
    q25 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='1P5')
    q26 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='1P6')
    q27 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='1P7')
    q28 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='1P8')
    q29 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='1P9')
    q30 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='1P10')

    q31 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='2M')
    q32 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='2P1')
    q33 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='2P2')
    q34 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='2P3')
    q35 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='2P4')
    q36 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='2P5')
    q37 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='2P6')
    q38 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='2P7')
    q39 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='2P8')
    q40 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='2P9')
    q41 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='2P10')

    q42 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='3M')
    q43 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='3P1')
    q44 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='3P2')
    q45 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='3P3')
    q46 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='3P4')
    q47 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='3P5')
    q48 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='3P6')
    q49 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='3P7')
    q50 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='3P8')
    q51 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='3P9')
    q52 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='3P10')

    q53 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='4M')
    q54 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='4P1')
    q55 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='4P2')
    q56 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='4P3')
    q57 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='4P4')
    q58 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='4P5')
    q59 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='4P6')
    q60 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='4P7')
    q61 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='4P8')
    q62 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='4P9')
    q63 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='4P10')

    q64 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='5M')
    q65 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='5P1')
    q66 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='5P2')
    q67 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='5P3')
    q68 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='5P4')
    q69 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='5P5')
    q70 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='5P6')
    q71 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='5P7')
    q72 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='5P8')
    q73 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='5P9')
    q74 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='5P10')

    q75 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='6M')
    q76 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='6P1')
    q77 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='6P2')
    q78 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='6P3')
    q79 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='6P4')
    q80 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='6P5')
    q81 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='6P6')
    q82 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='6P7')
    q83 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='6P8')
    q84 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='6P9')
    q85 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='6P10')

    q86 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='7M')
    q87 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='7P1')
    q88 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='7P2')
    q89 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='7P3')
    q90 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='7P4')
    q91 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='7P5')
    q92 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='7P6')
    q93 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='7P7')
    q94 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='7P8')
    q95 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='7P9')
    q96 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='7P10')

    q97 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='8M')
    q98 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='8P1')
    q99 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='8P2')
    q100 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='8P3')
    q101 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='8P4')
    q102 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='8P5')
    q103 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='8P6')
    q104 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='8P7')
    q105 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='8P8')
    q106 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='8P9')
    q107 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='8P10')

    q108 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='9M')
    q109 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='9P1')
    q110 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='9P2')
    q111 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='9P3')
    q112 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='9P4')
    q113 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='9P5')
    q114 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='9P6')
    q115 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='9P7')
    q116 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='9P8')
    q117 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='9P9')
    q118 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='9P10')

    q119 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='10M')
    q120 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='10P1')
    q121 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='10P2')
    q122 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='10P3')
    q123 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='10P4')
    q124 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='10P5')
    q125 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='10P6')
    q126 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='10P7')
    q127 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='10P8')
    q128 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='10P9')
    q129 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='10P10')


    q130 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='11M')
    q131 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='11P1')
    q132 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='11P2')
    q133 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='11P3')
    q134 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='11P4')
    q135 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='11P5')
    q136 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='11P6')
    q137 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='11P7')
    q138 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='11P8')
    q139 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='11P9')
    q140 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='11P10')

    q141 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='12M')
    q142 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='12P1')
    q143 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='12P2')
    q144 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='12P3')
    q145 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='12P4')
    q146 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='12P5')
    q147 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='12P6')
    q148 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='12P7')
    q149 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='12P8')
    q150 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='12P9')
    q151 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='12P10')

    q152 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='13M')
    q153 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='13P1')
    q154 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='13P2')
    q155 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='13P3')
    q156 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='13P4')
    q157 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='13P5')
    q158 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='13P6')
    q159 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='13P7')
    q160 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='13P8')
    q161 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='13P9')
    q162 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='13P10')

    q163 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='14M')
    q164 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='14P1')
    q165 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='14P2')
    q166 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='14P3')
    q167 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='14P4')
    q168 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='14P5')
    q169 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='14P6')
    q170 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='14P7')
    q171 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='14P8')
    q172 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='14P9')
    q173 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='14P10')

    q174 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='15M')
    q175 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='15P1')
    q176 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='15P2')
    q177 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='15P3')
    q178 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='15P4')
    q179 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='15P5')
    q180 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='15P6')
    q181 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='15P7')
    q182 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='15P8')
    q183 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='15P9')
    q184 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='15P10')

    q185 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='16M')
    q186 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='16P1')
    q187 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='16P2')
    q188 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='16P3')
    q189 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='16P4')
    q190 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='16P5')
    q191 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='16P6')
    q192 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='16P7')
    q193 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='16P8')
    q194 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='16P9')
    q195 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='16P10')

    q196 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='17M')
    q197 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='17P1')
    q198 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='17P2')
    q199 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='17P3')
    q200 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='17P4')
    q201 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='17P5')
    q202 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='17P6')
    q203 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='17P7')
    q204 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='17P8')
    q205 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='17P9')
    q206 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='17P10')

    q207 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='18M')
    q208 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='18P1')
    q209 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='18P2')
    q210 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='18P3')
    q211 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='18P4')
    q212 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='18P5')
    q213 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='18P6')
    q214 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='18P7')
    q215 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='18P8')
    q216 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='18P9')
    q217 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='18P10')

    q218 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='19M')
    q219 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='19P1')
    q220 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='19P2')
    q221 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='19P3')
    q222 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='19P4')
    q223 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='19P5')
    q224 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='19P6')
    q225 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='19P7')
    q226 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='19P8')
    q227 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='19P9')
    q228 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='19P10')

    q229 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='20M')
    q230 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='20P1')
    q231 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='20P2')
    q232 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='20P3')
    q233 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='20P4')
    q234 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='20P5')
    q235 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='20P6')
    q236 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='20P7')
    q237 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='20P8')
    q238 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='20P9')
    q239 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='20P10')

    q19 = models.TextField( unique=False, blank=True, verbose_name = 'Remarks')

    q1111 = models.IntegerField(choices=KRESULT, blank=False, verbose_name = 'Decision')
    q2222 = models.IntegerField(choices=ERESULT, blank=False, verbose_name = 'Rework by ')
    q3333 = models.CharField(max_length=200,blank=False, verbose_name = 'Cont. by')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.product) + str(self.created_on))
        super(Process_1, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Process 1 Start List'
        ordering = ['-created_on']
    def __str__(self):
        return self.slug

class Process_1_2(models.Model): #giriş kalite kontrol
    product = models.ForeignKey(Product, on_delete= models.CASCADE,related_name='product_process1_2', verbose_name = 'Hangi Ürün?')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL )   
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    q4444 = models.CharField(max_length=200, blank=False, verbose_name = 'Approvied by')    

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.product) + str(self.created_on))
        super(Process_1_2, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Process 1 End List'
       
        ordering = ['-created_on']
    def __str__(self):
        return self.slug


class Process_2(models.Model): #ön montaj
    product = models.ForeignKey(Product,  on_delete= models.CASCADE,related_name='product_process2')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL )   
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    q1 = models.IntegerField(choices=RESULT,  blank=False, verbose_name='1.I received the product file for pre assembly.')
    q2 = models.IntegerField(choices=RESULT,  blank=False, verbose_name = '2.I received the oil tank.')
    q3 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '3.I received the valve stand.')
    q4 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '4.I received the accumulator stand.')
    q5 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '5.All assembly parts are correct and there is no missing part')
    q6 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '6.Tank cover is Ok')
    q7 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '7.I received the blocks for power unit.')
    q8 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '8.Electric motor is checked ,size ,frequency and power is OK.')
    q9 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '9.Electric motor damping rods are OK')
    q10 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '10.Pumps are OK')
    q11 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '11.Bellhousng is suitable for pumps and electric motors.')
    q12 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '12.Couplings are OK for pumps and electric motors.')
    q13 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '13.Pumps flanges are OK')
    q14 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '14.Pressure filter is OK.')
    q15 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '15.Return filter is OK.')
    q16 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '16.Three way valve is OK and fit to Hydraulic circut.')
    q17 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '17.Accumulator/Accumulators are OK.')
    q18 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '18.Accumulator assembly parts are OK')
    q19 = models.IntegerField(choices=RESULT, blank=False, verbose_name = "19.Accumulator's safety block is OK")
    q20 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '20.Cooling type and size are OK for assembly.')
    q21 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '21.Compensator is OK')
    q22 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '22.Butterfly valves are OK.')
    q23 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '23.Tank drain valve is OK')
    q24 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '24.Heater  is OK and there is no problem for tank assembly.')
    q25 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '25.Level gauge is OK')
    q26 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '26.Level gauge with switch is OK.')
    q27 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '27.Manometer type and size is  OK')
    q28 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '28.Flange connections are OK')
    q29 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '29.Stainless fittings and pipes are OK.')
    q30 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '30.Silica gel / air filter is OK')
    q31 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '31.Terminal box is OK')
    q32 = models.TextField( unique=False, blank=True, verbose_name = 'Remarks')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.product) + str(self.created_on))
        super(Process_2, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Process 2 Start List'
        ordering = ['-created_on']
    def __str__(self):
        return self.slug

class Process_2_2(models.Model): #ön montaj2
    product = models.ForeignKey(Product,  on_delete= models.CASCADE,related_name='product_process2_2')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL )   
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)    

    q1 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '32.Pump-Electric Motor assemblied.')
    q2 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '33.Oil pan assemblied.')
    q3 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '34.Pump-Electric Motor group assemblied on tank')
    q4 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '35.Manifolds  tested')
    q5 = models.IntegerField(choices=RESULT, blank=False, verbose_name = "36.Manifolds's drain lines assemblied .")
    q6 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '37.According the flow direction, pressure filter assemblied and there is enough place for changing filter element.')
    q7 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '38.According to flow direction return filter assemblied.')
    q8 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '39.Accumulator assemblied.')
    q9 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '40.Air filter / silika gel type air filter assemblied.')
    q11 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '41.Hose connections types, size and lenghts defined and ordered.')
    q12 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '42.Manometer panel welded.')
    q13 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '43.Protection covers are welded of oil tank for heater or switches.')
    q14 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '44.terminal box connection profile welded.')
    q15 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '45.Valve stand assembly done')
    q16 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '46.Accumulator stand assembly done.')
    q17 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '47.Design department informed about all asssembly problems ')
    q18 = models.IntegerField(choices=RESULT, blank=False, verbose_name = '48.Manifold connection plates welded.')
    q19 = models.TextField( unique=False, blank=True, verbose_name = 'Remarks')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.product) + str(self.created_on))
        super(Process_2_2, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Process 2 End List'

        ordering = ['-created_on']
    def __str__(self):
        return self.slug

class Process_3(models.Model): #borulama
    product = models.ForeignKey(Product,  on_delete= models.CASCADE,related_name='product_process3')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL )   
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    q1 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'I checked out the assembly drawing and Hydraulic circut.')
    q2 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'According to design drawing all pipes can be manufacturable.')
    q3 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'All pipelines do not cause a problem for assembly of HPU.')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.product) + str(self.created_on))
        super(Process_3, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Process 3 Start List'

        ordering = ['-created_on']
    def __str__(self):
        return self.slug

class Process_3_2(models.Model): #borulama
    product = models.ForeignKey(Product,   on_delete= models.CASCADE,related_name='product_process3_2')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL )   
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    q1 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'Are the pipelines accordance with assembly drawing and hydraulic circut?')
    q2 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'Are the pipe diameters the same as stated in the hydraulic circuit?')
    q3 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'Are all pipe connections (service connections) or customer connections accessible?')
    q4 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'Are all hydraulic connections (screw connection of flanges and fittings) tight?')
    q5 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'Are all the pipes cleaned and preserved?')
    q6 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'Is there any evidence of unpermitted flattening? If there is no specific customer request, standard of DC; otherwise max. is 6% according to ko = [(Dmax – Dmin)/D ] x 100 ')
    q7 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'Were directions changes of piping avoid? It should be preferably used round arches, angle fittings should be avoided.')
    q8 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'They lay down specific requirements for suction and pressure lines and were these observed? (high dynamic range)')
    q9 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'Are the hoses fitted professionally? (bend radious not  too small and do not contact with other parts)')
    q10 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'If there is contact with other parts, the protection against abrasion been provided. ')
    q11 = models.IntegerField(choices=RESULT, blank=False, verbose_name = "The hose security chains been correctly fitted? Security chain lock's ring pressed.")
    q12 = models.TextField( unique=False, blank=True, verbose_name = 'Remarks')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.product) + str(self.created_on))
        super(Process_3_2, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Process 3 End List'

        ordering = ['-created_on']
    def __str__(self):
        return self.slug

class Process_4(models.Model): #kaynak
    product = models.ForeignKey(Product,  on_delete= models.CASCADE,related_name='product_process4')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL )   
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    q1 = models.IntegerField(choices=RESULT, blank=False, verbose_name = "I have already taken information about the material were used for piping and oil tank' mataerial. The used WPS is selected the materials of oil tank and pipes material accordingly.")
    q2 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'Before spot welding of cleaning covers of oil tank, I made spot welding and check the parameters of Welding.')
    q3 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'All surfaces were cleaned by rust, paint or oil before welding.')
    
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.product) + str(self.created_on))
        super(Process_4, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Process 4 Start List'

        ordering = ['-created_on']
    def __str__(self):
        return self.slug


class Process_4_2(models.Model): #kaynak
    product = models.ForeignKey(Product,  on_delete= models.CASCADE,related_name='product_process4_2')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL )   
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    q4 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'I welded the cleaning  covers than checked the position of cleaning cover on tank.')
    q5 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'I welded the grounding element to oil tank.')
    q6 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'I applied TIG welding process for root pass of pipe. I applied the MAG welding for cover passess for pipe.')
    q7 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'I checked root after root pass of pipe welding. If there is sagging, I cleaned it with stone engine, grinder.')
    q8 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'I checked undercuts after cover pass.')
    q9 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'I checked start and finish point of MAG welds.')
    q10 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'I cleaned surfaces and applied passivation liquied for stainless materials welding process.')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.product) + str(self.created_on))
        super(Process_4_2, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Process 4 End List'

        ordering = ['-created_on']
    def __str__(self):
        return self.slug

class Process_5(models.Model): #boya
    product = models.ForeignKey(Product,  on_delete= models.CASCADE,related_name='product_process5')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL )   
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    q0 = models.IntegerField(unique=False, blank=False, verbose_name='Ral Code:')
    q1 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'I checked the all surfaces for components of assemby parts and oil tank ( from outside and inside). All surfaced cleaned by rust, dirt and oil.')
    q2 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'I checked paint type of request in order form and masked the related surfaces of Power Unit. ( including the rubber and plastic parts) ')
    q3 = models.TextField( unique=False, blank=True, verbose_name = 'Remarks')


    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.product) + str(self.created_on))
        super(Process_5, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Process 5 Start List'

        ordering = ['-created_on']
    def __str__(self):
        return self.slug

class Process_5_2(models.Model):
    product = models.ForeignKey(Product,  on_delete= models.CASCADE,related_name='product_process5_2')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL )   
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    q1 = models.IntegerField(choices=RESULT,blank=False, verbose_name = 'The HPU is painted as requested in order form.')
    q2 = models.IntegerField(choices=RESULT,blank=False, verbose_name = 'There is no any surface as not painted and surface quality of paint as requested.')
    q3 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'If there is surface where is extended out of HPU and has a risk for safety the related are is painted with different color.')
    q4 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'I waited the dryin period and than checked the hardness of paint.')
    q5 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'All preventive masks removed after painting')
    q6 = models.IntegerField(default=234 ,blank=False, verbose_name = 'I measured the thickness of paint.')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.product) + str(self.created_on))
        super(Process_5_2, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Process 5 End List'

        ordering = ['-created_on']
    def __str__(self):
        return self.slug

class Process_6(models.Model): #son montaj
    product = models.ForeignKey(Product,  on_delete= models.CASCADE,related_name='product_process6')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL )   
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    q1 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'I checked out the paint hardness and all painted surfaces.')
    q2 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'There is no unpainted surface.')
    q3 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'There is no orange peeling on surfaces.')
    q4 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'The tank inside’s surface is free of contamination.')


    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.product) + str(self.created_on))
        super(Process_6, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Process 6 Start List'
        ordering = ['-created_on']
    def __str__(self):
        return self.slug

class Process_6_2(models.Model): #son montaj
    product = models.ForeignKey(Product,  on_delete= models.CASCADE,related_name='product_process6_2')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL )   
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    q1 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'The all manifolds assemblied on tank')
    q2 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'The cooler installed.')
    q3 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'Air filter installed.')
    q4 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'Silica gel installed.')
    q5 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'Thermostat installed')
    q6 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'Temprature/Level gauge installed')
    q7 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'Level Switch installed')
    q8 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'Pressure line filter installed in accordance with flow direction.')
    q9 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'Return line filter installed in accordance with flow direction.')
    q10 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'Accumulator installed')
    q11 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'Manometers installed.')
    q12 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'Are all hydraulic connections done and  (pipings,screw connection of flanges and fittings) tighted.')
    q13 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'Heater installed.')
    q14 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'Hose lenght controlled')
    q15 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'Hose connection fittings types controlled')
    q16 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'Security ropes controlled of hoses')
    q17 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'the production date of hoses controlled. ( its allowed the hose produces in last 2 years) ')
    q18 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'Hose pressure values compared with HPU test pressure')
    q19 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'The hoses fitted professionaly. (e.g. Bend radii not too small. In case of contact with other parts scoring protector used)')
    q20 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'If there is contact with other parts, the protection against abrasion been provided.')
    q21 = models.IntegerField(choices=RESULT, blank=False, verbose_name = 'The hose security chains been correctly fitted? Secure chains lock were pressed.')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.product) + str(self.created_on))
        super(Process_6_2, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Process 6 End List'

        ordering = ['-created_on']
    def __str__(self):
        return self.slug

def Process7_image(instance, filename): 
    return 'Product_Pictures/{0}/Process7/{1}'.format(instance.product, filename)

class Process_7(models.Model):
    product = models.ForeignKey(Product,  on_delete= models.CASCADE,related_name='product_process7')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL )   
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    q1 = models.IntegerField(choices=ARESULT, blank=False, verbose_name = 'I check out the Hydraulic circut.')
    q2 = models.IntegerField(choices=ARESULT, blank=False, verbose_name = 'I check out the test pressure.')
    q3 = models.IntegerField(choices=ARESULT, blank=False, verbose_name = 'I check out the set up values of valves accodance with Hydraulic circut.')
    q4 = models.IntegerField(choices=ARESULT, blank=False, verbose_name = 'I checked out the ıf there special test requirements or test plans.')
    q5 = models.IntegerField(choices=ARESULT, blank=False, verbose_name = 'All electrical connections are done by electric technician.')
    q6 = models.IntegerField(choices=ARESULT, blank=False, verbose_name = 'Oil tank is filled with oil.')
    q7 = models.IntegerField(choices=ARESULT, blank=False, verbose_name = 'Im going to increase the pressure quit slowly when I start the pressure test.')

    p1 = models.ImageField(upload_to=Process7_image, blank=True, null=True, verbose_name='Upload Image 1')
    p2 = models.ImageField(upload_to=Process7_image, blank=True, null=True, verbose_name='Upload Image 2')
    p3 = models.ImageField(upload_to=Process7_image, blank=True, null=True, verbose_name='Upload Image 3')
    p4 = models.ImageField(upload_to=Process7_image, blank=True, null=True, verbose_name='Upload Image 4')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.product) + str(self.created_on))
        super(Process_7, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Process 7 Start List'
        ordering = ['-created_on']
    def __str__(self):
        return self.slug


class Process_7_2(models.Model):
    product = models.ForeignKey(Product,  on_delete= models.CASCADE,related_name='product_process7_2')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL )   
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    q6 = models.IntegerField(choices=ARESULT, blank=False, verbose_name = 'Assemb. Control')
    q7 = MultiSelectField(choices=Multiple, max_choices=14, blank=True, verbose_name = 'Elec.Mot.Return Dir.')
    q8 = models.IntegerField(choices=ARESULT, blank=False, verbose_name = 'Hose Control')
    q9 = models.IntegerField(choices=ARESULT, blank=False, verbose_name = 'Fittings Control')
    q10 = models.IntegerField(choices=ARESULT, blank=False, verbose_name = 'Return Fittings Control')
    q11 = models.IntegerField(choices=ARESULT, blank=False, verbose_name = 'Function Test')
    q12 = models.IntegerField(choices=YYRESULT, blank=False, verbose_name = 'Oil Leakage')
    q13 = models.IntegerField(choices=CRESULT, blank=False, verbose_name = 'Missing Parts')
    q14 = models.IntegerField(choices=ARESULT, blank=False, verbose_name = 'Oil reservoir has been checked from inside after test ')
    q15 = models.TextField(unique=False, blank=True, verbose_name = 'Remarks')

    q16 = models.IntegerField(default=0 ,unique=False, blank=True, verbose_name = 'Ral Code For First Coat')
    q17 = models.IntegerField(default=0 ,unique=False, blank=True, verbose_name = 'Ral Code For Second Coat')
    q18 = models.IntegerField(default=0 ,unique=False, blank=True, verbose_name = 'Thickness For Prime Coat')
    q19 = models.IntegerField(default=0 ,unique=False, blank=True, verbose_name = 'Thickness For Second Coat')

    q21 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 1 : Pz')
    q37 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 1 : Bar') 

    q22 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 2 : Pz')
    q38 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 2 : Bar')

    q23 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 3 : Pz')
    q39 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 3 : Bar')

    q24 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 4 : Pz')
    q40 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 4 : Bar')

    q25 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 5 : Pz')
    q41 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 5 : Bar')

    q26 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 6 : Pz')
    q42 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 6 : Bar')

    q27 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 7 : Pz')
    q43 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 7 : Bar')

    q28 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 8 : Pz')
    q44 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 8 : Bar')

    q29 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 9 : Pz')
    q45 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 9 : Bar')

    q30 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 10 : Pz')
    q46 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 10 : Bar')

    q31 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 11 : Pz')
    q47 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 11 : Bar')

    q32 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 12 : Pz')
    q48 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 12 : Bar')

    q33 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 13 : Pz')
    q49 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 13 : Bar')

    q34 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 14 : Pz')
    q50 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 14 : Bar')

    q35 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 15 : Pz')
    q51 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 15 : Bar')

    q36 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 16 : Pz')
    q52 = models.CharField(max_length=200, unique=False, blank=True,verbose_name='Valve 16 : Bar')

    q20 = models.TextField(unique=False, blank=True, verbose_name = 'Remarks')

    q1 = models.CharField(max_length=200, blank=True, verbose_name = 'Tested By')
    q2 = models.CharField(max_length=200, blank=True, verbose_name = 'Controlled By')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.product) + str(self.created_on))
        super(Process_7_2, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Process 7 End List'
        ordering = ['-created_on']
    def __str__(self):
        return self.slug

def Process8_image(instance, filename): 
    return 'Product_Pictures/{0}/Process8/{1}'.format(instance.product, filename)

class Process_8(models.Model): #son kontrol
    product = models.ForeignKey(Product,  on_delete= models.CASCADE,related_name='product_process8')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL )   
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    q1 = models.IntegerField(choices=KKARESULT, blank=False, verbose_name = 'Cleanliness,Oil,Paint Failure')
    q2 = models.IntegerField(choices=KKARESULT, blank=False, verbose_name = 'Deformation, Rust')
    q3 = models.IntegerField(choices=KKARESULT, blank=False, verbose_name = 'Open holes closed')
    q4 = models.IntegerField(choices=KKARESULT, blank=False, verbose_name = 'Missing Component')
    q5 = models.IntegerField(choices=KKARESULT, blank=False, verbose_name = 'Hose Pressure Limit / Security Rope')
    q6 = models.IntegerField(default=0, blank=False, verbose_name = 'Paint Thickness')
    q7 = models.IntegerField(choices=KKARESULT, blank=False, verbose_name = 'WARNING Labels')
    q8 = models.IntegerField(choices=KKARESULT, blank=False, verbose_name = 'Press. Filter Flow Direction')
    q9 = models.IntegerField(choices=KKARESULT, blank=False, verbose_name = 'Oil Leakage')
    q10 = models.IntegerField(choices=KKARESULT, blank=False, verbose_name = 'Documentation')
    q11 = models.IntegerField(choices=KKARESULT, blank=False, verbose_name = 'Lifting Eyes')
    q12 = models.IntegerField(choices=KKARESULT, blank=False, verbose_name = 'Traceability Labe')
    q13 = models.IntegerField(choices=KKARESULT, blank=False, verbose_name = 'Marker of Prod. Employee')
    q14 = models.IntegerField(choices=KKARESULT, blank=False, verbose_name = 'Other Assembly Part Package')

    content = models.TextField(unique=False, blank=True, verbose_name = 'Remarks')

    picture1 = models.ImageField(upload_to=Process8_image, blank=True, null=True, verbose_name='Upload Image 1')
    picture2 = models.ImageField(upload_to=Process8_image, blank=True, null=True, verbose_name='Upload Image 2')
    picture3 = models.ImageField(upload_to=Process8_image, blank=True, null=True, verbose_name='Upload Image 3')
    picture4 = models.ImageField(upload_to=Process8_image, blank=True, null=True, verbose_name='Upload Image 4')
    picture5 = models.ImageField(upload_to=Process8_image, blank=True, null=True, verbose_name='Upload Image 5')
    picture6 = models.ImageField(upload_to=Process8_image, blank=True, null=True, verbose_name='Upload Image 6')
    picture7 = models.ImageField(upload_to=Process8_image, blank=True, null=True, verbose_name='Upload Image 7')
    picture8 = models.ImageField(upload_to=Process8_image, blank=True, null=True, verbose_name='Upload Image 8')
    picture9 = models.ImageField(upload_to=Process8_image, blank=True, null=True, verbose_name='Upload Image 9')
    picture10 = models.ImageField(upload_to=Process8_image, blank=True, null=True, verbose_name='Upload Image 10')




    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.product) + str(self.created_on))
        super(Process_8, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Process 8 Start List'
        ordering = ['-created_on']
    def __str__(self):
        return self.slug


class Process_8_2(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE,related_name='product_process8_2')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL )   
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    q1111 = models.IntegerField(choices=KRESULT,  blank=False, verbose_name = 'Result')
    q3333 = models.CharField(default=" ", max_length=200, blank=False, verbose_name = 'Controller')
    q4444 = models.CharField(default=" ", max_length=200, blank=False, verbose_name = 'Approving Person')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.product) + str(self.created_on))
        super(Process_8_2, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Process 8 End List'

        ordering = ['-created_on']
    def __str__(self):
        return self.slug

"""
class Process_2_TR(models.Model): #ön montaj
    product = models.ForeignKey(Product, on_delete= models.CASCADE,related_name='product_process2')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL )   
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    #sorular
    q1 = models.IntegerField(choices=RESULT, default=0, blank=True, verbose_name='Ön montaj için ürün dosyasını teslim aldım.')
    q2 = models.IntegerField(choices=RESULT, default=0, blank=True, verbose_name = 'Tank teslim alınmıştır.')
    q3 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Valf standı teslim alınmıştır.')
    q4 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Akü standın teslim alınmıştır.')
    q5 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Montaj için gerekli diğer sac parçalar doğru ve eksiksizdir. ')
    q6 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Depo kapakları doğrudur . ')
    q7 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Ünite blokları teslim alınmıştır.')
    q8 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Elektrik motoru doğrudur. Yapı büyüklüğü ve kW cinsinden ')
    q9 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Elektrik motoru titreşim takozları doğrudur.')
    q10 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Pompalar doğrudur.')
    q11 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Kampana elektrik motoru ve pompaya uygundur.')
    q12 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Kaplin takımı elektrik motoru ve pompaya uygundur.')
    q13 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Dişli pompa montaj flanşları temin edilmiştir.')
    q14 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Basınç filtresi doğrudur')
    q15 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Dönüş filtresi doğrudur.')
    q16 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Dönüş filtresi temizliği için kullanılan 3 yollu küresel vana doğrudur. ')
    q17 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Akü/aküler doğrudur')
    q18 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Akü montaj kelepçe ve plakaları doğrudur.')
    q19 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Akü emniyet bloğu doğrudur. ')
    q20 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Soğutucu doğrudur. Montaj yeri açısından ')
    q21 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Kompansatör doğrudur.')
    q22 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Kelebek vana doğrudur.')
    q23 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Tank tahliye kürsel vanası doğrudur.')
    q24 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Isıtıcı doğrudur. Tankta perde sacı veya diğer bir ekipmana çarpmamaktadır')
    q25 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Seviye göstergeleri doğrudur. ')
    q26 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Seviye şalteri doğrudur. ')
    q27 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Manometreler doğrudur. ')
    q28 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Minimes rekoru doğrudur. ')
    q29 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Minimes hortumu doğrudur.')
    q30 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Bağlantı flanşları doğrudur. ')
    q31 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Paslanmaz fittingsler ve borular doğrudur.')
    q32 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Yansanayien temin edilen borular doğrudur.')
    q33 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Nem alıcı (silikajel) / hava filtresi doğrudur.')
    q34 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Klemens kutusu doğrudur. ')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.product) + 'process-2-1')
        super(Process_2, self).save(*args, **kwargs)
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.slug

class Process_2_2_TR(models.Model): #ön montaj2
    product = models.ForeignKey(Product, on_delete= models.CASCADE,related_name='product_process2_2')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL )   
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)    

    q35 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Akuplaj eksiksiz monte edilmiştir.')
    q36 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Akuplajda yağ tavası varsa montajı yapılmıştır.')
    q37 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Akuplajın tanka montajı yapılmıştır.')
    q38 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Bloklar test ettirilmiştir. ')
    q39 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Blokların tank geri dönüş boruları monte edilmiş ve tanka montajı tamamlanmıştır. ')
    q40 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Basınç filtresi montajı yağ giriş yönü kontrol edilerek yapılmış ve filtre elemanını değiştirmek için yeterli alan vardır.')
    q41 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Dönüş filtresi montajı yağ giriş yönü kontrol edilerek yapılmıştır.')
    q42 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Soğutcu montajı filtresi montajı yağ giriş yönü kontrol edilerek yapılmıştır.')
    q43 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Akü montajı yapılmıştır.')
    q44 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Hava filtresi / nem alıcı (silikajel) monte edilmiştir.')
    q45 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Hortum bağlantıları ve ölçüleri belirlenmiş ve sipariş edilmiştir.')
    q46 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Manometre sacı kaynatılmış ve manometreler monte edilmiştir.')
    q47 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Transmitter, termostat gibi tanka montajı yapılan montaj parçalarının koruma sacları kaynatılmış ve parçalar monte edilmiştir.')
    q48 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Klemens kutusu sacı kaynatılmıştır.')
    q49 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Valf standı montajı eksiksiz yapılmıştır.')
    q50 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Akü standı montajı eksiksiz yapılmıştır.')
    q51 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Montaj ve demontaj işlemlerinde zorluk çıkartabilecek borulamalar önceden tespit edilmiş ve tasarım bölümüne bilgi verilmiştir.')
    q52 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Blok bağlantı lamaları kaynakları tamamlanmıştır.')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.product) + 'process-2-2')
        super(Process_2_2, self).save(*args, **kwargs)
    content = models.TextField()
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.slug

class Process_3(models.Model): #borulama
    product = models.ForeignKey(Product, on_delete= models.CASCADE,related_name='product_process3')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL )   
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    q1 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Montaj ve demontaj işlemlerinde zorluk çıkartabilecek borulama yoktur.')
    q2 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Pompa ana dağıtım bloğu borulaması yapılmıştır.')
    q3 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Pompa basınç filtresi borulaması yapılmıştır.')
    q4 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Basınç filtresi ana dağıtım bloğu borulaması yapılmıştır.')
    q5 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Dişli pompa tespit plakası nipeli ve tespit plakası nipelinden ana dağıtım bloğuna borulama yapılmıştır.')
    q6 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Bloklar arası borulama yapılmıştır. ')
    q7 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Tank hattı soğutucu - dönüş filtresi borulaması yapılmıştır. ')
    q8 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Sirkülasyon hattı borulaması pompa/ soğutucu/ dönüş filtresi arasında yapılmıştır.')
    q9 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Tank hattı- küresel vana (bypass sistemi)  ve dönüş filtresi borulaması yapılmıştır. ')
    q10 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Akü hattı borulaması yapılmıştır.')
    q11 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Akü standı borulaması yapılmıştır.')
    q12 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Valf standı borulaması yapılmıştır. ')
    q13 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Yapılan bütün borulamalar devre şemasına göre yapılmıştır.')
    q14 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Kullanılan boru çapları devre şemasında belirtilen çaplara ve et kalınlıklarına uygundur.')
    q15 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Bütün boru bağlantılarına ( servis ve müşteri bağlantıları) rahatça ulaşılabiliyor.')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.product) + 'process-3-1')
        super(Process_3, self).save(*args, **kwargs)
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.slug


class Process_4_TR(models.Model): #kaynak
    product = models.ForeignKey(Product, on_delete= models.CASCADE,related_name='product_process4')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL )   
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    q1 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Kaynak işleminden önce yapılması gereken borulama ve kaynak işlemleri hakkında bilgi aldım, kaynaklanacak malzeme türlerini öğrendim ve WPS lerimi kontrol ettim.')
    q2 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Depo kapağından önce örnek bir sacta saplama kaynağı yaparak koparma testi gerçekleştirdim.')
    q3 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Bütün kaynak işlemlerinden önce kaynak yapılacak yüzeyleri yağdan, pas ve vb kirden arındırdım. ')
    q4 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Depo kapağı saplama kaynaklarını yaptım ve kapak montajını yaparak boyutsal doğruluğunu kontrol ettim. ')
    q5 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Topraklama civatası kaynağını yaptım')
    q6 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Boru/dirsek / flanş kaynaklarında kök kaynağını TIG ve dolgu pasoları MAG ile gerçekleştirdim. ')
    q7 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Kök kaynağı işinden sonra kökte sarkma olup olmadığını kontrol ettim. Sarkma varsa taş moturu ile temizledim.')
    q8 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Kapak pasolarda yanma oluklarının oluşup oluşmadığını kontrol ettim. ')
    q9 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'MAG kaynaklarında başlangıç ve bitiş hatası kontrollerini gerçekleştirdim.')
    q10 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Montak parçaları (kablo kanalı, filtre konsolu…vb)  kaynaklarında da yukarıdaki kaynak kontrollerini gerçekleştirdim.')
    q11 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Paslanmaz kaynak işlemlerinden sonra yüzey temizleme ve pasivasyon işlemlerini gerçekleştirdim. ')
    q12 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Kaldırma kancalarını kaynatmadan önce yüzeydeki astarı temizledim ve sonrasında kaynak işlemini yaptım. ')
    
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.product) + 'process-4-1')
        super(Process_4, self).save(*args, **kwargs)
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.slug

class Process_5_TR(models.Model): #boya
    product = models.ForeignKey(Product, on_delete= models.CASCADE,related_name='product_process5')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL )   
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    q1 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Boya işlemi öncesi Tankı / Akuplajları / Akü - Valf standını ve montaj parçalarını inceledim ve astar yanıklarını paslı, çizik kirli ve çizik/ darbe almış yüzeyleri tespit ettim ve gerekli boya öncesiz hazırlıkları yaptım.')
    q2 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Boya işleminden önce gerekli montaj parçalarını maskeledim ve boya işlemini sipariş formundaki isteklere göre gerçekleştirdim.')
    q3 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Kaldırma kulaklarını sarı renkle boyadım')
    q4 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Tank üzerinde dışarı çıkıntı yapan yüzeyler veya sivri noktalar varsa sarı renkle boyadım.')
    q5 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Boya sonrası gerekli kuruma süresini beklettim. ')
    q6 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Boya sonrası tank içi temizliği gerçekleştirdim. ')
    q7 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Boya sonrası yapılan maskelemeleri söktüm ve boyanmamış ve rütuş isteyen yüzeyleri tespit edip gerekli boya işlemleri yaptım.')
    q8 = models.IntegerField(choices=RESULT,  default=0 ,blank=True, verbose_name = 'Boya Kalınlığı ölçümünü gerçekleştirdim')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.product) + 'process-5-1')
        super(Process_5, self).save(*args, **kwargs)
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.slug

class Process_6_TR(models.Model): #son montaj
    product = models.ForeignKey(Product, on_delete= models.CASCADE,related_name='product_process6')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL )   
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    q1 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Blok montajlarını gerçekleştirdim.')
    q2 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Soğutucu montajını gerçekleştirdim. ')
    q3 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Hava filtresi monte edilmiştir.')
    q4 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Nem alıcı (silikajel) monte edilmiştir.')
    q5 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Termostatlar monte edilmiştir.')
    q6 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Seviye/sıcaklık göstergesi monte edilmiştir.')
    q7 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Seviye şalteri monte edilmiştir.')
    q8 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Basınç filtresi montajı yağ giriş yönü kontrol edilerek yapılmıştır.')
    q9 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Dönüş filtresi montajı yağ giriş yönü kontrol edilerek yapılmıştır.')
    q10 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Soğutucu montajı yapılmıştır.')
    q11 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Akü montajı yapılmıştır.')
    q12 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Manometreler onte edilmiştir.')
    q13 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Isıtıcı montajı yapılmıştır.')
    q14 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Sipariş edilen hortumların boyları kontrol edilmiştir.')
    q15 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Sipariş edilen hortumların bağlantı rekorları kontrol edilmiştir.')
    q16 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Sipariş edilen hortumların emniyet kabloları konrol edilmiştir.')
    q17 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Sipariş edilen hortumların imalat tarihi kabul edilmiş ve içinde bulunduğumuz yıl dahil olmak üzere son 2 yıl içinde üretilmiş bir hortumdur.')
    q18 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Hortum basınç değerleri sistemin çalışma ve test basıncından daha büyük değerdedir.')
    q19 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Hortumların monte edildiği alanda, hortumun basıncın etkisiyle hareket etmesi sonucu sürtüneceği başka bir montaj parçası yoktur. ')
    q20 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Tüm hidrolik bağlantıların (dirsekler, rekorlar ..vb)  montajı uygun torklar ile sıkılmıştır.')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.product) + 'process-6-1')
        super(Process_6, self).save(*args, **kwargs)
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.slug

class Process_7(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE,related_name='product_process7')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL )   
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    q1 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Montaj Kontrol')
    q2 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Elek.mot.Dön.Yön./ ')
    q3 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Hortum Kntrl')
    q4 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Fittings Kntrl')
    q5 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Dön.Filt.Kntrl.')
    q6 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Fonk. Test ')
    q7 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Yağ Kaçağı')
    q8 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Komponentler')
    q9 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Devre Şema No/Hyd.Circuit No')
    q10 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Açıklamlar/Remarks')
    q11 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Komponentler')
    q12 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Komponentler')
    q13 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Komponentler')
    q14 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Komponentler')
    q15 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Komponentler')
    q16 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Komponentler')
    q17 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Komponentler')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.product) + 'process-7-1')
        super(Process_7, self).save(*args, **kwargs)
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.slug

class Process_8_TR(models.Model): #son kontrol
    product = models.ForeignKey(Product, on_delete= models.CASCADE,related_name='product_process8')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL )   
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    q1 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Temizlik, Boya Dökülmesi, Çapak, yağ tavasında ve tank yüzeyinde yağ')
    q2 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Darbe, Pas')
    q3 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Açık hatlar uygun kapaklarla kapatılmıştır ')
    q4 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Eksik Malzeme')
    q5 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Hortum Basinç Degeri ve Hortum Kelepçesi')
    q6 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Boya Kalinligi')
    q7 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'UYARI Etiketleri (Elektrik motoru dönüs yönü, Akü çalisma basinci)')
    q14 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Basinç Filtresi')
    q8 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Yag Kacagi (Koir tapa kullanimi)')
    q9 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Dokümantasyon')
    q10 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Kaldirma Kulaklar')
    q11 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Ünite Etiketi')
    q12 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Etikete Numaratör Vurulmus mu?')
    q13 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Tank yaninda gidecek malzemelerin paketlenmesi')
    q15 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Kontrol Eden')
    q16 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Onaylayan')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.product) + 'process-8-1')
        super(Process_8, self).save(*args, **kwargs)
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.slug

"""



