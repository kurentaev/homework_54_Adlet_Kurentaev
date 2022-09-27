from django.db import models


class Products(models.Model):
    title = models.TextField(max_length=1000, null=False, blank=False, default='None', verbose_name='Наименование')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    category = models.ForeignKey(
        verbose_name='Категория',
        to='webapp.Categories',
        null=False,
        blank=False,
        related_name='categories',
        on_delete=models.RESTRICT,
        default=None
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    price = models.DecimalField(max_digits=19, decimal_places=0, verbose_name='Стоимость')
    image = models.TextField(
        max_length=1000,
        null=False,
        blank=False,
        default='https://99px.ru/sstorage/56/2015/01/image_560401151755269388068.jpg',
        verbose_name='Изображение'
    )

    def __str__(self):
        return f"{self.title} - {self.description} - {self.category} - {self.price}"


class Categories(models.Model):
    category = models.TextField(max_length=200, null=True, blank=True, default=1, verbose_name='Категория')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return f"{self.category}"
