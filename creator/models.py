from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Creator(models.Model):
    user = models.OneToOneField(User, related_name='content_creator',on_delete=models.CASCADE)
    profile = models.ImageField(upload_to='profile_photo_folder',default='pic_folder/None/no-img.jpg',verbose_name='profile_photo')
    bio = models.CharField(max_length=300,default='edit - e.g Teacher at Gauteng School')
    social_url = models.URLField(name='social-media-url',default='www.example.com')
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username