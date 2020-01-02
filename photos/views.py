from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    images = Image.objects.all()
    
    return render(request,'home.html',{"images":images})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/image.html", {"image":image})


