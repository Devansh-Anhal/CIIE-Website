from django.shortcuts import render
from .models import Image,Category

# Create your views here.

def gallery(request):
	cat=request.GET.get('event', '')
	if cat:
		catId=Category.objects.get(category=cat)
		pics = Image.objects.filter(category=catId)
		return render(request,'eventgallery.html',{'pics':pics, 'category':cat})
	categories = Category.objects.all()
	return render(request,'gallery.html',{'categories':categories})


