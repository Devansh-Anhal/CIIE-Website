from django.shortcuts import render
from .models import idea,join, startup
from django.shortcuts import redirect
import sweetify
from NUciie.utils import render_to_pdf 
from django.template.loader import get_template
from django.http import HttpResponse



from .forms import ideaForm, joinForm, incubationForm
# Create your views here.
def ideaView(request):
	template="idea.html"

	if request.method == "POST":
		form = ideaForm(request.POST)
		if form.is_valid():
			form.save()
			sweetify.success(request, 'Your Idea was submitted', text='', persistent='Ok')
			return redirect('/idea')

	else:
		form = ideaForm()

	context = {
		'form' : form ,
	}			

	return render(request, template, context)

def joinView(request):
	template="join.html"

	if request.method == "POST":
		form = joinForm(request.POST)

		if form.is_valid():
			form.save()
			sweetify.success(request, 'Your request was submitted', text='', persistent='Ok')
			return redirect('/joinus')

	else:
		form = joinForm()

	context = {
		'form' : form 
	}			

	return render(request, template, context)

def incubView(request):
	template="startup.html"

	if request.method == "POST":
		form = incubationForm(request.POST)

		if form.is_valid():
			form.save()
			sweetify.success(request, 'Your application was submitted', text='', persistent='Ok')
			return redirect('/startupform')

	else:
		form = incubationForm()

	context = {
		'form' : form ,
	}			

	return render(request, template, context)


def joinPDF(request, object_id):
	obj=join.objects.get(pk=object_id)

	template = get_template('pdfjoin.html')
	html = template.render({'obj':obj})

	pdf = render_to_pdf('pdfjoin.html',{'obj':obj})
	if pdf:
		response = HttpResponse(pdf, content_type='application/pdf')
		filename = obj.first_name+".pdf"
		content = "inline; filename=%s" %(filename)
		download = request.GET.get("download")
		if download:
			content = "attachment; filename=%s" %(filename)
		response['Content-Disposition'] = content
		return response
	return HttpResponse("Not found")

def ideaPDF(request, object_id):
	obj=idea.objects.get(pk=object_id)

	template = get_template('pdfIdea.html')
	html = template.render({'obj':obj})

	pdf = render_to_pdf('pdfIdea.html',{'obj':obj})
	if pdf:
		response = HttpResponse(pdf, content_type='application/pdf')
		filename = obj.first_name+".pdf"
		content = "inline; filename=%s" %(filename)
		download = request.GET.get("download")
		if download:
			content = "attachment; filename=%s" %(filename)
		response['Content-Disposition'] = content
		return response
	return HttpResponse("Not found")

def startupPDF(request, object_id):
	obj=startup.objects.get(name_of_enterprise=object_id)
	template = get_template('pdfstartup.html')
	html = template.render({'obj':obj})

	pdf = render_to_pdf('pdfstartup.html',{'obj':obj})
	if pdf:
		response = HttpResponse(pdf, content_type='application/pdf')
		filename = obj.name_of_enterprise+".pdf"
		content = "inline; filename=%s" %(filename)
		download = request.GET.get("download")
		if download:
			content = "attachment; filename=%s" %(filename)
		response['Content-Disposition'] = content
		return response
	return HttpResponse("Not found")