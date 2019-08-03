from django.contrib import admin
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.dispatch import receiver
from import_export.admin import ImportExportMixin
from .models import Event,Registration, nustartup
from django.conf import settings


class EventAdmin(ImportExportMixin, admin.ModelAdmin):
	list_display=('title',)
	def post_save():
		print('updated')

admin.site.register(Event, EventAdmin)

class RegisterAdmin(ImportExportMixin, admin.ModelAdmin):
	list_display=('event','registrant',)
admin.site.register(Registration, RegisterAdmin)

@receiver(post_save, sender=Event)
def mail_handler(sender,instance, **kwargs):
	registrant_list = Registration.objects.filter(event=instance).only("registrant")
	mailing_list=[]   
	for registrant in registrant_list:
		mailing_list.append(str(registrant.registrant))
	# subject = 'Event updated'
	# message = 'event has been updated'
	# email_from = settings.EMAIL_HOST_USER
	# send_mail( subject, message, email_from, mailing_list )

admin.site.register(nustartup)