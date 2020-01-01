from django.db import models

# Create your models here.

class Profile(models.Model):
    username = models.TextField(max_length=40)
    bio = models.CharField(max_length= 100)
    def __str__(self):
        return self.username

class Image(models.Model):
    image_name= models.CharField(max_length=60)
    profile =models.ForeignKey('Profile',on_delete=models.CASCADE,)
    def __str__(self):
        return self.image_name


