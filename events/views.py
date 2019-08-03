from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from .models import Event, Registration,nustartup
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.
def events(request):
	events =  dict.fromkeys(Event.objects.all()[::-1], 0)
	if request.user.is_authenticated:
		user  = request.user
		registerdEvents= Registration.objects.filter(registrant=user)
		for i in events:
			for reg in registerdEvents:
				if i==reg.event :
					events[i]=1
	return render(request,'events.html',{'events':events})

def submit(request):
	if request.method == 'POST':
		if request.user.is_authenticated:
			event= request.POST['event']
			try:
				go = Event.objects.get(title=event)
			except SomeModel.DoesNotExist:
				go = None
			user  = request.user
			exists= Registration.objects.filter(event=go, registrant=user).count()
			r= Registration(event=go, registrant=user)
			if exists:
				Registration.objects.filter(event=go, registrant=user).delete()
			else:
				r.save()
	return HttpResponse('')


def event_details(request):
	id=request.GET.get('id', '')	#Get attribute from url
	event=Event.objects.get(pk=id)	#get model from database by id
	return render(request,'event_details.html',{'event':event}) #send model to view renderer 


def startups(request):
	startups=nustartup.objects.all()
	return render(request,'startup/startups.html',{'startups':startups})


def startup(request):
	id=request.GET.get('id', '')	#Get attribute from url
	startup=nustartup.objects.get(pk=id)	#get model from database by id
	return render(request,'startup/startupPage.html',{'startup':startup}) #send model to view renderer 
