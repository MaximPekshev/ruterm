# Generated by Django 3.2.6 on 2021-09-27 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogapp', '0004_category_title_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='meta_description_en',
            field=models.TextField(blank=True, max_length=1024, null=True, verbose_name='meta description'),
        ),
        migrations.AddField(
            model_name='good',
            name='meta_name_en',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='meta name'),
        ),
    ]
