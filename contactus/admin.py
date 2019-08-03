from django.contrib import admin
from .models import idea,join,startup
from .views import joinPDF, ideaPDF, startupPDF
from django.utils.html import format_html

# Register your models here.
@admin.register(join)
class AccountAdmin(admin.ModelAdmin):
	date_heirarchy = (
		'modified',
	)
	list_display = (
		'first_name',
		'last_name',
		'email',
		'enrollment_no',
		'generate_pdf_preview_html',
	)

	readonly_fields = (
		'first_name',
		'last_name',
		'email',
		'enrollment_no',
		'why_do_you_want_to_join_CIIE',
	)
	 
	def generate_pdf_preview_html(self, obj):
		return format_html('<a class="button" href="%s/joinPDF/">Export as PDF</a>' % obj.id)
		
	generate_pdf_preview_html.short_description = 'Generate pdf preview'
	generate_pdf_preview_html.allow_tags = True

	def get_urls(self):
		from django.urls import path

		urls = super().get_urls()
		custom_urls = [path('<path:object_id>/joinPDF/', self.admin_site.admin_view(joinPDF),
				 name='vision_questionarioistituzionescolastica_generatepdf')
		]

		return custom_urls + urls


@admin.register(idea)
class AccountAdmin(admin.ModelAdmin):
	date_heirarchy = (
		'modified',
	)
	list_display = (
		'first_name',
		'last_name',
		'email',
		'enrollment_no',
		'generate_pdf_preview_html',
	)

	readonly_fields = (
		'first_name',
		'last_name',
		'email',
		'enrollment_no',
		'idea',
		'why_do_you_want_to_join_CIIE',
	)
	 
	def generate_pdf_preview_html(self, obj):
		return format_html('<a class="button" href="%s/ideaPDF/">Export as PDF</a>' % obj.id)
		
	generate_pdf_preview_html.short_description = 'Generate pdf preview'
	generate_pdf_preview_html.allow_tags = True

	def get_urls(self):
		from django.urls import path

		urls = super().get_urls()
		custom_urls = [path('<path:object_id>/ideaPDF/', self.admin_site.admin_view(ideaPDF),
				 name='vision_questionarioistituzionescolastica_generatepdf')
		]

		return custom_urls + urls

@admin.register(startup)
class AccountAdmin(admin.ModelAdmin):
	date_heirarchy = (
		'modified',
	)
	list_display = (
		'name_of_enterprise',
		'name_of_enterpreneur',
		'generate_pdf_preview_html',
	)

	 
	def generate_pdf_preview_html(self, obj):
		return format_html('<a class="button" href="%s/startupPDF/">Export as PDF</a>' % obj.name_of_enterprise)
		
	generate_pdf_preview_html.short_description = 'Generate pdf preview'
	generate_pdf_preview_html.allow_tags = True

	def get_urls(self):
		from django.urls import path

		urls = super().get_urls()
		custom_urls = [path('<path:object_id>/startupPDF/', self.admin_site.admin_view(startupPDF),
				 name='vision_questionarioistituzionescolastica_generatepdf')
		]

		return custom_urls + urls
