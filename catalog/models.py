from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='products/', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, verbose_name='категория', **NULLABLE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена за покупку')
    date_of_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    date_of_last_change = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['-date_of_create']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='название категории')
    description = models.TextField(verbose_name='описание категории', **NULLABLE)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name
