from django.db import models


class Category(models.Model):
    is_published = models.BooleanField('Опубликовано', default=True)
    name = models.CharField('Название', max_length=200)
    slug = models.SlugField('Слаг', max_length=200)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class Item(models.Model):
    published = models.BooleanField('Опубликовано', default=True)
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    on_main = models.BooleanField('На главную?', default=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='items',
        blank=True,
        null=True
    )
