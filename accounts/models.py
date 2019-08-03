from django.db import models
from django.contrib.auth.models import(
		BaseUserManager, AbstractBaseUser
	)
from django.core.validators import RegexValidator
import hashlib 


NAME_REGEX = '^[a-zA-Z]+$'

# Create your models here.
class UserManager(BaseUserManager):
	def create_user(self,username, email, password = None):
		if not email:
			raise ValueError('User must have email')

		user = self.model(
				username   = username,
				email	   = self.normalize_email(email),
				FirstName  = username.split('.')[0],
				LastName   = username.split('.')[1],
			)

		user.set_password(password)
		user.save(using = self._db)
		return user

	def create_superuser(self, email, password = None):
		SUser = self.create_user(
				username='admin.admin', email=email, password=password
			)
		SUser.is_staff= True
		SUser.save(using = self._db)
		return SUser


class CUser(AbstractBaseUser):

	objects = UserManager()

	username = models.CharField(max_length=16,default=0)

	email = models.EmailField(
				max_length=255,
				unique= True,
				verbose_name= 'email address'
			)
	FirstName = models.CharField(
				max_length=300,
				validators = [
					RegexValidator( regex= NAME_REGEX,
									message='Name should contain only alphabets',
									code= 'invalid_name')
					]
			)

	LastName = models.CharField(
				max_length=300,
				validators = [
					RegexValidator( regex= NAME_REGEX,
									message='Name should contain only alphabets',
									code= 'invalid_name')
					]
			)	


	is_staff = models.BooleanField(default=False)

	object= UserManager()

	USERNAME_FIELD = 'email'
	

	def __str__(self):
		return self.email

	def get_short_name(self):
		# The user is identified by their email address
		return self.email


	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True
