# Generated by Django 4.1 on 2022-08-20 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0013_category_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='name',
        ),
    ]
