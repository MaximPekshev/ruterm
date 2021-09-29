from django.db import models
import uuid

from uuslug import slugify

def get_uuid():
	return str(uuid.uuid4().fields[0])

def get_image_name(instance, filename):
	
	new_name = ('%s' + '.' + filename.split('.')[-1]) % instance.cpu_slug
	return new_name

class Category(models.Model):

	title 				= models.CharField(max_length = 150, verbose_name='Наименование')
	title_en			= models.CharField(max_length = 150, verbose_name='Наименование на английском', blank=True,)
	description 		= models.TextField(max_length=10240, verbose_name='Описание', blank=True, null=True)
	description_en 		= models.TextField(max_length=2048, verbose_name='Описание на английском', blank=True)
	meta_name 			= models.CharField(max_length=150, verbose_name='meta name', blank=True, null=True)
	meta_description 	= models.TextField(max_length=1024, verbose_name='meta description', blank=True, null=True)
	meta_name_en 		= models.CharField(max_length=150, verbose_name='meta name', blank=True, null=True)
	meta_description_en	= models.TextField(max_length=1024, verbose_name='meta description', blank=True, null=True)
	cpu_slug			= models.SlugField(max_length=70, verbose_name='ЧПУ_Url', blank=True, db_index=True)
	picture				= models.ImageField(upload_to=get_image_name, verbose_name='Изображение 870x502', default=None, null=True, blank=True)


	def __str__(self):

		return self.title

	def save(self, *args, **kwargs):

		self.cpu_slug = '{}'.format(slugify(self.title))	

		super(Category, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'		
	

class Good(models.Model):
	
	cpu_slug			= models.SlugField(max_length=70, verbose_name='ЧПУ_Url', blank=True, db_index=True)
	title 				= models.CharField(max_length = 150, verbose_name='Наименование')
	title_en			= models.CharField(max_length = 150, verbose_name='Наименование на английском', blank=True,)
	description 		= models.TextField(max_length=2048, verbose_name='Описание', blank=True)
	description_en 		= models.TextField(max_length=2048, verbose_name='Описание на английском', blank=True)

	meta_name 			= models.CharField(max_length=150, verbose_name='meta name', blank=True, null=True)
	meta_description 	= models.TextField(max_length=1024, verbose_name='meta description', blank=True, null=True)

	meta_name_en 		= models.CharField(max_length=150, verbose_name='meta name', blank=True, null=True)
	meta_description_en	= models.TextField(max_length=1024, verbose_name='meta description', blank=True, null=True)

	good_type 			= models.CharField(max_length = 150, verbose_name='Тип', blank=True, null=True)
	good_lenght			= models.CharField(max_length = 150, verbose_name='Длина', blank=True, null=True)
	good_height			= models.CharField(max_length = 150, verbose_name='Высота', blank=True, null=True)
	good_depth 			= models.CharField(max_length = 150, verbose_name='Глубина', blank=True, null=True)
	operating_pressure  = models.CharField(max_length = 150, verbose_name='Рабочее давление', blank=True, null=True)
	test_pressure  		= models.CharField(max_length = 150, verbose_name='Испытательное давление', blank=True, null=True)
	coolant_temperature = models.CharField(max_length = 150, verbose_name='Максимальная температура теплоносителя', blank=True, null=True)
	rf_certificate  	= models.CharField(max_length = 150, verbose_name='Сертификат соответствия РФ', blank=True, null=True)
	color  				= models.CharField(max_length = 150, verbose_name='Цвет', blank=True, null=True)
	surface_treatment_technology = models.CharField(max_length = 150, verbose_name='Технология обработки поверхности', blank=True, null=True)
	guarantee  			= models.CharField(max_length = 150, verbose_name='Гарантия', blank=True, null=True)

	category 			= models.ForeignKey('Category', verbose_name='Категория', on_delete=models.SET_DEFAULT,null=True, blank=True, default=None)


	def __str__(self):

		return self.title

	def save(self, *args, **kwargs):

		self.cpu_slug = '{}'.format(slugify(self.title))	

		super(Good, self).save(*args, **kwargs)
			
	def get_main_image(self):

		main_image = Picture.objects.filter(good=self, main_image=True).first()
		if main_image:
			return main_image
		else:
			return Picture.objects.filter(good=self).first()	


	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

def get_image_name_for_product(instance, filename):
	
	new_name = ('%s' + '.' + filename.split('.')[-1]) % instance.slug
	return new_name

class Picture(models.Model):

	title 					= models.CharField(max_length=150, verbose_name='Наименование', blank=True)
	slug 					= models.SlugField(max_length=36, verbose_name='Url', blank=True, db_index=True)
	good 					= models.ForeignKey('Good', verbose_name='Товар', on_delete=models.CASCADE)
	images					= models.ImageField(upload_to=get_image_name_for_product, verbose_name='Изображение 369x419', default=None)
	main_image				= models.BooleanField(verbose_name='Основная картинка', default=False)

	def __str__(self):
		
		return self.slug

	def save(self, *args, **kwargs):
		
		if self.slug == "":
			self.slug = get_uuid()
			self.title = self.slug

		super(Picture, self).save(*args, **kwargs)
	
	class Meta:
		
		verbose_name = 'Картинка'
		verbose_name_plural = 'Картинки'		