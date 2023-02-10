from django.db import models
from django.urls import reverse
# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    photo = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category_mp', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

class Category_mp(models.Model):

    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title



class Goods(models.Model):
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    title = models.CharField(max_length=300, verbose_name='Наименование товара')
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('about_good', kwargs={'slug_cat': self.category.slug, 'slug_good_name': self.slug})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:

        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Gallery(models.Model):
    image = models.ImageField(upload_to='goods/%Y/%m/%d', blank=True)
    good = models.ForeignKey('Goods', on_delete=models.CASCADE, verbose_name='Изображение', related_name='images')


    def get_absolute_url(self, img=False):
        # current_img = self.image.url.split('/')[-1].split('.')[0]
        current_img = self.image.url.replace('/', '-').replace('.', '_')

        return reverse('current_img', kwargs={
            'slug_cat': self.good.category.slug,
            'slug_good_name': self.good.slug,
            'current_img': current_img,
        })



