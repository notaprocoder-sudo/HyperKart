from django.db import models
from django.urls import reverse


# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('Fakekartapp:PbyC', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='product', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('Fakekartapp:procatdetail', args=[self.category.slug, self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.name)
