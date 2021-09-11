from django.db import models
from django.conf import settings
from django.urls import reverse




class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    cat_name = models.CharField(max_length=100, unique=True, verbose_name='Category')
    slug = models.SlugField(unique=True)
    cat_img = models.ImageField(blank=True, null=True, verbose_name='Category Image', help_text='Use this Image dimension 170px X 100px')
    cat_img_banner = models.ImageField(blank=True, null=True, verbose_name='Category Banner Image', help_text='Use this Image dimension 848px X 132px')
    created = models.DateTimeField(auto_now_add=True)

    def show_cat_img(self):
        if self.cat_img:
            return self.cat_img.url
        else:
            return 'prairiemartapp/images/media/index1/img-categori2.jpg'

    def show_cat_img_banner(self):
        if self.cat_img_banner:
            return self.cat_img_banner.url

    def __str__(self):
        return self.cat_name

    class Meta():
        verbose_name_plural = 'Category'
        ordering = ['-created',]

    def save(self, *args, **kwargs):
        self.cat_name = self.cat_name.capitalize()
        return super().save(*args, **kwargs)

class Brand(models.Model):
    brand_name = models.CharField(max_length=30, unique=True, verbose_name='Brand')
    slug = models.SlugField(unique=True)
    brand_img = models.ImageField(blank=True, null=True, verbose_name='Brand Image', help_text='Use this Image dimension 157px X 88px')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.brand_name

    class Meta():
        verbose_name_plural = 'Brand'
        ordering = ['-created',]
    
    def show_cat_img(self):
        if self.brand_img:
            return self.brand_img.url
        else:
            return 'prairiemartapp/images/media/index1/top-brand2.png'

    def save(self, *args, **kwargs):
        self.cat_name = self.brand_name.capitalize()
        return super().save(*args, **kwargs)


class Size(models.Model):
    size = models.CharField(max_length=15, unique=True, help_text='Size Name')
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.size

    class Meta():
        verbose_name_plural = 'Size'
        ordering = ['-created',]
    

    def save(self, *args, **kwargs):
        self.size = self.size.upper()
        return super().save(*args, **kwargs)
    

class Products(models.Model):
    prod_name = models.CharField(max_length=300, verbose_name='Product Name')
    slug = models.SlugField(max_length=300, unique=True)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name='product_brand', null=True, blank=True, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, related_name='product_size', null=True, blank=True, on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_creator')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    image1 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image2 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image3 = models.ImageField(upload_to='uploads/', blank=True, null=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = models.Manager()

    class Meta:
        verbose_name_plural='Products'
        ordering = ('-created',)

    def show_image1(self):
        if self.image1:
            return self.image1.url
        else:
            return 'prairiemartapp/images/media/index1/top-brand2.png'

    def show_image2(self):
        if self.image2:
            return self.image2.url
        else:
            return 'prairiemartapp/images/media/index1/top-brand2.png'

    def show_image3(self):
        if self.image3:
            return self.image3.url
        else:
            return 'prairiemartapp/images/media/index1/top-brand2.png'
    
    def get_absolute_url(self):
        return reverse('prairiemartapp:product_detail', args=[self.slug])

    def __str__(self):
        return self.prod_name