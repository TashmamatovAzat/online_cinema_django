from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название жанра')

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название фильма')
    year = models.CharField(max_length=10, verbose_name='Год выпуска фильма')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание фильма')
    country = models.CharField(max_length=100, verbose_name='Страна выпуска фильма')
    image = models.ImageField(upload_to = 'images/', verbose_name='Главная картинка', max_length=250)
    video = models.FileField(upload_to = 'videos/', verbose_name='Видео')

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=20)
