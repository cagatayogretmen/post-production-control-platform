from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_photo = models.ImageField(null=True, blank = True, upload_to='user_pictures', default='default.png')
    dep = models.CharField(max_length=20)
    position = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'User Profile'
    
    def __str__(self):
        return self.user.username
