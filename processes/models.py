from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.timezone import now
from django.conf import settings


STATUS = (
    (0,"In Process"),
    (1,"Controlled")
)

RESULT = (
    (0, 'Evet'),
    (1, 'Hayır'),
    (2, 'İlgili Değil')
)

sorular = ['soru1','soru2','soru3','soru4','soru5']


class Product(models.Model):
    Userr= request.user.username
    product_name = models.CharField(max_length=200, verbose_name='Ürün İsmi')
    created_by = models.ForeignKey(Userr,editable=False,null=True,blank=True,  on_delete = models.CASCADE)    
    status = models.IntegerField(choices=STATUS, default=0, verbose_name='Durum')
    slug = models.SlugField(max_length=200, unique=True)
    production_order_no = models.CharField(max_length=200, unique=False, blank=True, verbose_name='Üretim Sipariş No')
    order_position_no = models.CharField(max_length=200, unique=False, blank=True, verbose_name='Sipariş Pozisyon No')
    reference_no = models.CharField(max_length=200, unique=False, blank=True, verbose_name='Referans No')
    quantity = models.CharField(max_length=200, unique=False, blank=True, verbose_name='Adet')
    working_pressure = models.CharField(max_length=200, unique=False, blank=True, verbose_name='Sistem Çalışma Basıncı')
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='product_pictures/', blank=True , verbose_name='Fotoğraf Yükle')
    content = models.TextField(blank=True, verbose_name='Açıklama' )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.product_name

class Process_1(models.Model): #giriş kalite kontrol
    product = models.ForeignKey(Product, on_delete= models.CASCADE,related_name='product_process1', verbose_name = 'Hangi Ürün?')
    created_by = models.ForeignKey(User, on_delete= models.CASCADE,related_name='user_process1')    
    status = models.IntegerField(choices=STATUS, default=0 ,verbose_name='Durum')  
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)



    soru1 = models.IntegerField(choices=RESULT, default=0, blank=True, verbose_name='Hidrolik Güç Ünitesi izlenebilirlik etiketi takılmıştır.')
    soru2 = models.IntegerField(choices=RESULT, default=0, blank=True, verbose_name = 'Montajçılar, kaynakçılar ve testçiler ünite izlenebilirlik kartını işaretlemişlerdir')
    soru3 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Hidrolik Güç Ünitesinde (HGÜ) herhangi bir görsel uygunsuzluk (darbe, kirlilik, pas, boya) yoktur.')

    content = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.slug


class Process_2(models.Model): #ön montaj
    product = models.ForeignKey(Product, on_delete= models.CASCADE,related_name='product_process2')
    created_by = models.ForeignKey(User, on_delete= models.CASCADE,related_name='user_process2', )    
    status = models.IntegerField(choices=STATUS, default=0)  
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

    for soru in sorular:
        exec("%s = models.IntegerField(choices=RESULT, default=0)" % (soru))
    content = models.TextField()

    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.slug

class Process_3(models.Model): #borulama
    product = models.ForeignKey(Product, on_delete= models.CASCADE,related_name='product_process3')
    created_by = models.ForeignKey(User, on_delete= models.CASCADE,related_name='user_process3')    
    status = models.IntegerField(choices=STATUS, default=0)  
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




    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.slug


class Process_4(models.Model): #kaynak
    product = models.ForeignKey(Product, on_delete= models.CASCADE,related_name='product_process4')
    created_by = models.ForeignKey(User, on_delete= models.CASCADE,related_name='user_process4')    
    status = models.IntegerField(choices=STATUS, default=0)  
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

    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.slug

class Process_5(models.Model): #boya
    product = models.ForeignKey(Product, on_delete= models.CASCADE,related_name='product_process5')
    created_by = models.ForeignKey(User, on_delete= models.CASCADE,related_name='user_process5')    
    status = models.IntegerField(choices=STATUS, default=0)  
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
    q8 = models.IntegerField(choices=RESULT, default=0 ,blank=True, verbose_name = 'Boya Kalınlığı ölçümünü gerçekleştirdim')

    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.slug

class Process_6(models.Model): #son montaj
    product = models.ForeignKey(Product, on_delete= models.CASCADE,related_name='product_process6')
    created_by = models.ForeignKey(User, on_delete= models.CASCADE,related_name='user_process6')    
    status = models.IntegerField(choices=STATUS, default=0)  
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
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.slug

class Process_7(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE,related_name='product_process7')
    created_by = models.ForeignKey(User, on_delete= models.CASCADE,related_name='user_process7')    
    status = models.IntegerField(choices=STATUS, default=0)  
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    for soru in sorular: #unite test raporu
        exec("%s = models.IntegerField(choices=RESULT, default=0)" % (soru))
    content = models.TextField()

    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.slug

class Process_8(models.Model): #son kontrol
    product = models.ForeignKey(Product, on_delete= models.CASCADE,related_name='product_process8')
    created_by = models.ForeignKey(User, on_delete= models.CASCADE,related_name='user_process8')    
    status = models.IntegerField(choices=STATUS, default=0)  
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    for soru in sorular:
        exec("%s = models.IntegerField(choices=RESULT, default=0)" % (soru))
    content = models.TextField()

    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.slug
