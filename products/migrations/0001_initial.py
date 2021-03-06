# Generated by Django 2.1.5 on 2021-09-14 01:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=30, unique=True, verbose_name='Brand')),
                ('slug', models.SlugField(unique=True)),
                ('brand_img', models.ImageField(blank=True, help_text='Use this Image dimension 157px X 88px', null=True, upload_to='', verbose_name='Brand Image')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Brand',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=100, unique=True, verbose_name='Category')),
                ('slug', models.SlugField(unique=True)),
                ('cat_img', models.ImageField(blank=True, help_text='Use this Image dimension 170px X 100px', null=True, upload_to='', verbose_name='Category Image')),
                ('cat_img_banner', models.ImageField(blank=True, help_text='Use this Image dimension 848px X 132px', null=True, upload_to='', verbose_name='Category Banner Image')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.Category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'Category',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=300, verbose_name='Product Name')),
                ('slug', models.SlugField(max_length=300, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('in_stock', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_brand', to='products.Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.Category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(help_text='Size Name', max_length=15, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Size',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='products',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_size', to='products.Size'),
        ),
    ]
