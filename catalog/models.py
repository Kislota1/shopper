from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='имя категории')
    description = models.TextField(verbose_name='описание категории')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'имя категории'
        verbose_name_plural = 'имя категорий'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='продукт')
    description = models.TextField(verbose_name='описание')
    photo = models.ImageField(upload_to='catalog/', verbose_name='фото', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    unit_price = models.IntegerField(verbose_name='цена')
    creation_date = models.DateTimeField(verbose_name='дата создания')
    modified_date = models.DateTimeField(verbose_name='дата изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
