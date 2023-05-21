from django.contrib.auth.models import User
from django.db import models


class Advert(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст объявления')
    image = models.ImageField(upload_to='avert-images/', verbose_name='Фотография')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    accepted_reply = models.ForeignKey('Reply', on_delete=models.CASCADE, null=True, verbose_name='Принятый отклик',
                                       related_name='accepted_reply')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.title}'


class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE, verbose_name='Объявление')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Отклик '
        verbose_name_plural = 'Отклики'

    def __str__(self):
        return f'Отклик № {self.id} Автор: {self.author}'
