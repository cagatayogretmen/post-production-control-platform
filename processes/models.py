from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.timezone import now

STATUS = (
    (0,"In Process"),
    (1,"Controlled")
)

RESULT = (
    (0, 'No'),
    (1, 'Yes'),
    (2, 'Not relevant')
)

sorular = ['soru1','soru2','soru3','soru4','soru5']


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete= models.CASCADE,related_name='user_product')    
    status = models.IntegerField(choices=STATUS, default=0)
    slug = models.SlugField(max_length=200, unique=True)
    production_order_no = models.CharField(max_length=200)
    order_position_no = models.CharField(max_length=200)
    reference_no = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    working_pressure = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='images/', blank=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.product_name

class Process_first(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE,related_name='product_process1')
    created_by = models.ForeignKey(User, on_delete= models.CASCADE,related_name='user_process1')    
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


    
class Process_second(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE,related_name='product_process2')
    created_by = models.ForeignKey(User, on_delete= models.CASCADE,related_name='user_process2')    
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


class Process_three(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE,related_name='product_process3')
    created_by = models.ForeignKey(User, on_delete= models.CASCADE,related_name='user_process3')    
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
