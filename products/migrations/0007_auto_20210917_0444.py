# Generated by Django 2.1.5 on 2021-09-17 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210917_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='old_price',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]