# Generated by Django 3.0.5 on 2020-10-06 21:52

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctions',
            name='auction_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='auctions',
            name='feature',
            field=ckeditor.fields.RichTextField(verbose_name='Özellikler'),
        ),
    ]
