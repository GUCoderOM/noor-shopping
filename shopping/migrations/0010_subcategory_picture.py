# Generated by Django 4.1 on 2022-08-17 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0009_product_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='picture',
            field=models.ImageField(blank=True, upload_to='../static/product_images'),
        ),
    ]
