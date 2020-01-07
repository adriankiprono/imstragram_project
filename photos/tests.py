from django.test import TestCase
from . models import * 

# Create your tests here.
class ImageTestClass(TestCase):
    '''
    This is a class that perform unnittest  behaviour on the Image Model.
    '''
    
    def setUp(self):
        
        self.image_one = Image(image='images/lagoon.jpeg',name='bombklat',)
     