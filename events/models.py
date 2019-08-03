from django.db import models
from accounts.models import CUser


# Create your models here.
class Event(models.Model):
	title		= models.CharField(max_length=255)
	description = models.TextField(default='insert');
	logo		= models.ImageField(upload_to = "events",default='default.jpg', blank=True)

	def __str__(self):
		return self.title

class Registration(models.Model):
	event = models.ForeignKey(Event, on_delete = models.CASCADE)
	registrant =  models.ForeignKey(CUser,  on_delete = models.CASCADE)

class nustartup(models.Model):
	title		= models.CharField(max_length=255)
	description = models.TextField(default='insert')
	team        = models.TextField(default='insert')
	logo		= models.ImageField(upload_to = "events",default='default.jpg', blank=True)
	url			= models.CharField(max_length=255)
	
	def __str__(self):
		return self.title