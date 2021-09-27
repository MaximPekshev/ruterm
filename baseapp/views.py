from django.shortcuts import render
from catalogapp.models import Category

def show_index(request):
	return render(request, 'baseapp/index.html')

def show_production(request):
	return render(request, 'baseapp/production.html')

def show_about_company(request):
	return render(request, 'baseapp/about.html')

def show_products(request):
	context = {
		'categories' : Category.objects.all()
	}
	return render(request, 'baseapp/products.html', context)

def show_contacts(request):
	return render(request, 'baseapp/contacts.html')	

