from django.shortcuts import render
from catalogapp.models import Category

def en_show_index(request):
	return render(request, 'en_baseapp/en_index.html')


def en_show_production(request):
	return render(request, 'en_baseapp/en_production.html')

def en_show_about(request):
	return render(request, 'en_baseapp/en_about.html')

def en_show_contact(request):
	return render(request, 'en_baseapp/en_contact.html')	

def en_show_products(request):
	context = {
		'categories' : Category.objects.all()
	}
	return render(request, 'en_baseapp/en_products.html', context)

def en_show_documents(request):
	return render(request, 'en_baseapp/en_documents.html')	