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
    image = models.ImageField(verbose_name='Главная картинка')
    video = models.FileField(verbose_name='Видео')

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    def __str__(self):
        return self.name
