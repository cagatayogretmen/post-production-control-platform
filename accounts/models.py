from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, )
    profile_photo = models.ImageField(null=True, blank = True, verbose_name = 'Profil verbose')


    class Meta:
        verbose_name_plural = 'Kullanıcı'
    
    def get_screen_name(self):
        user = self.user
        if user.get_fu

    def get_userprofile_photo(self):
        if self.profile_photo:
            return self.profile_photo.url
        return "static/dist/img/avatar.png"


    def __str__(self):
        return self.user_name