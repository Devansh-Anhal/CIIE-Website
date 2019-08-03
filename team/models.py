from django.db import models

# Create your models here.

class Title(models.Model):
	title= models.CharField(max_length=255)
	priority = models.IntegerField(default=0, null=False)
	def __str__(self):
		return self.title


class Member(models.Model):
	title = models.ForeignKey(Title, on_delete = models.CASCADE)
	name  = models.CharField(max_length=255)
	phone = models.CharField(max_length=10)
	email = models.EmailField(null=True)
	image = models.ImageField(upload_to = "team", default='default.jpg', blank=True)
	url   = models.CharField(max_length=255, default="#")

	def __str__(self):
		return self.name