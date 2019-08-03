from django.db import models

# Create your models here.
class Category(models.Model):
	category 	= models.CharField(primary_key=True,max_length=255, default="All")
	thumbnail	= models.ImageField(upload_to = "gallery/category", default='default.jpg', blank=True)
	def __str__(self):
		return self.category

class Image(models.Model):
	category 	= models.ForeignKey(Category, on_delete = models.CASCADE,default=0)
	title		= models.CharField(max_length=255, default="enter")
	description = models.TextField(default='insert');
	image		= models.ImageField(upload_to = "gallery/images", default='default.jpg', blank=True)

	def __str__(self):
		return self.title