from django.shortcuts import render

def en_show_index(request):
	return render(request, 'en_baseapp/en_index.html')


def en_show_production(request):
	return render(request, 'en_baseapp/en_production.html')