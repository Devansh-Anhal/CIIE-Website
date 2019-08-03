from django.contrib import admin

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreationForm
from .models import CUser

# Register your models here.
from social_django.models import Association, Nonce, UserSocialAuth

admin.site.unregister(Association)
admin.site.unregister(Nonce)
admin.site.unregister(UserSocialAuth)


class UserAdmin(BaseUserAdmin):
	add_form = UserCreationForm

	list_display = ('email','FirstName', 'LastName', 'is_staff')
	list_filter = ('is_staff',)

	fieldsets = (
			(None, {'fields': ('username','email','FirstName', 'LastName','password')}),
			('Permissions', {'fields': ('is_staff',)})
		)

	search_fields = ('username','email',)
	ordering = ('username','email',)

	filter_horizontal = ()


admin.site.register(CUser, UserAdmin)


admin.site.unregister(Group)