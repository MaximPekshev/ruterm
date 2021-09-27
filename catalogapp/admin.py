from django.contrib import admin
from .models import  Category
from .models import Good, Picture
from django.utils.safestring import mark_safe

class CategoryAdmin(admin.ModelAdmin):
	list_display = (
					'title',
					'cpu_slug',
					)
	readonly_fields = ('cpu_slug',) 

admin.site.register(Category, CategoryAdmin)


class PictureInline(admin.TabularInline):
    model = Picture

    fields = (
    			'images',
    			'main_image',
    	)

    exclude = ('title', 'slug')
    extra = 0

class GoodAdmin(admin.ModelAdmin):

	list_display = (
					'title',
					'title_en',
					'cpu_slug',
					'image',

					)

	list_filter = ('category',)

	inlines 	 = [PictureInline]

	search_fields = ('title', )

	exclude = ('cpu_slug',)

	def formfield_for_foreignkey(self, db_field, request, **kwargs):

		if db_field.name == "category":
			kwargs["queryset"] = Category.objects.all()
			return super(GoodAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
		

	def image(self, obj):

		img = Picture.objects.filter(good=obj, main_image=True).first() if Picture.objects.filter(good=obj, main_image=True).first() else Picture.objects.filter(good=obj).first()
		if img:
			return mark_safe('<img src="{url}" width="50" />'.format(url=img.images.url))
		else:
			return ''	

admin.site.register(Good, GoodAdmin)    