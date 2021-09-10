from django.db import models
from django.conf import settings
from django.shortcuts import reverse


# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=100, unique=True, verbose_name='Category Name', blank=True, null=True, )
    cat_desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.cat_name

    class Meta():
        verbose_name_plural = 'Category'

    def save(self, *args, **kwargs):
        self.cat_name = self.cat_name.capitalize()
        return super().save(*args, **kwargs)


class Post(models.Model):
    pst_title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    pst_image = models.ImageField('Post Image', blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    content = models.TextField('Content')
    created = models.DateTimeField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pst_title

    @property
    def img_url(self):
        if self.pst_image:
            return self.pst_image.url

    def get_post_url(self):
        return reverse('blog:blog_detail', kwargs={
            'slug': self.slug,
        })
