from django.shortcuts import render
from catalogapp.models import Category, Good
import xlrd
import os

def en_show_category(request, cpu_slug):

	category = Category.objects.filter(cpu_slug=cpu_slug).first()
	products = Good.objects.filter(category=category)

	context = {
		'category' : category,
		'products' : products,
	}

	return render(request, 'en_catalogapp/en_category.html', context)


def en_show_product_detail(request, cpu_slug):

	try:
		product = Good.objects.get(cpu_slug=cpu_slug)
	except:
		product = None

	context = {
		'product' : product,

	}

	if product.good_type:
		
		size = []
		weight = []
		mounting = []
		heat_head = []
		heat_head_1 = []
		heat_body = []

		try:
			book = xlrd.open_workbook(os.path.abspath('baseapp/static/files/type{}_en.xls'.format(product.good_type)))
		except:
			book = None

		if book:

			size_sh = book.sheet_by_index(0)
			for rx in range(size_sh.nrows):
				size.append(size_sh.row(rx))

			weight_sh = book.sheet_by_index(2)
			for rx in range(weight_sh.nrows):
				weight.append(weight_sh.row(rx))

			mounting_sh = book.sheet_by_index(3)
			for rx in range(mounting_sh.nrows):
				mounting.append(mounting_sh.row(rx))

			heat_sh = book.sheet_by_index(1)
			for rx in range(2):
				heat_head.append(heat_sh.row(rx))
			heat_head_1 = heat_sh.row(2)
			for rx in range(heat_sh.nrows)[3:]:
				heat_body.append(heat_sh.row(rx))

	context = {
		'product' : product,
		'size':size,
		'weight':weight,
		'mounting':mounting,
		'heat_head' : heat_head,
		'heat_body' : heat_body,
		'heat_head_1' : heat_head_1,

	}			

	return render(request, 'en_catalogapp/en_product_detail.html', context)
