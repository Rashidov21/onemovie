# Generated by Django 3.2.6 on 2022-05-24 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0010_auto_20220524_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likedmovielist',
            name='movie',
            field=models.ManyToManyField(blank=True, related_name='user_liked_movies', to='movie.Movie'),
        ),
    ]
