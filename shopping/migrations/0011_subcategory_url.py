# Generated by Django 4.1 on 2022-08-17 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0010_subcategory_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
