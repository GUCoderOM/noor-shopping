# Generated by Django 4.1 on 2022-08-18 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0011_subcategory_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='picture',
            field=models.ImageField(blank=True, upload_to='../static/product_images'),
        ),
    ]
