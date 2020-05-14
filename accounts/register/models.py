from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class deneme(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_photo = models.ImageField(null=True, blank = True)
    dep = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'User Settings'

    def __str__(self):
        return self.user.username

