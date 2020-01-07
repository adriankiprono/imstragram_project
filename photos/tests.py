from django.test import TestCase
from . models import * 

# Create your tests here.
class ImageTestClass(TestCase):
    '''
    This is a class that perform unnittest  behaviour on the Image Model.
    '''
    
    def setUp(self):
        
        self.image_one = Image(image='images/lagoon.jpeg',name='bombklat',)
 def test_instance(self):
        Image.objects.all().delete()
        self.assertTrue(isinstance(self.image_one,Image)) 

    def test_save_method(self):
        
        self.image_one.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        self.image_one.save_image()
        self.image_one.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) is 0)
        
    def test_update_method(self):
        self.image_one.save()
        
        done = self.image_one.(self.image_one.id,)
        self.assertEqual(done)
        
    def tearDown(self):
        Image.objects.all().delete()   
    
class ProfileTestClass(TestCase):
    
    '''
    This is a class that perform unnittest  behaviour on the Profile Model.
    '''
    
    def setUp(self):
        self.profile_one = Profile(profile_photo='images/mine.jpg',bio='Currently doing datascience in moringa',username="falone")
        
       
        