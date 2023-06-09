# Generated by Django 4.2 on 2023-04-29 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.CharField(max_length=250, verbose_name='Главная картинка'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='video',
            field=models.FileField(upload_to='', verbose_name='Видео'),
        ),
    ]
