# Generated by Django 2.1.5 on 2021-09-17 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210917_0413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='prod_price',
            new_name='price',
        ),
    ]
