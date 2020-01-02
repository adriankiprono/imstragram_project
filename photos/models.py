from django.db import models

# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=40)
    bio = models.TextField(max_length= 100)
    def __str__(self):
        return self.username
    
    

    

class Image(models.Model):
    image_name= models.CharField(max_length=60)
    profile =models.ForeignKey('Profile',on_delete=models.CASCADE,)
    image= models.ImageField(upload_to= 'images/',default='image')
    def __str__(self):
        return self.image_name
        
    @classmethod
    def search_by_name(cls,search_term):
        name = cls.objects.filter(name__icontains=search_term)
        return username


