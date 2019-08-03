from django.shortcuts import render
from .models import Title,Member
# Create your views here.
def team(request):
	titles = Title.objects.all().order_by('priority')
	dic={}
	for title in titles:
		members=Member.objects.filter(title=title)
		dic.update({members:title})
	return render(request,'team.html',{'dic':dic})

	# Create your views here.
def wedo(request):
	return render(request,'wedo.html')