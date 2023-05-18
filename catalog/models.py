from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)
    subscribe = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Company(models.Model):
    name = models.CharField(max_length=200)
    biography = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Games(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/', blank=True)
    subscribe = models.TextField()
    date_created = models.DateField()
    rating = models.FloatField(blank=True)
    count_player = models.FloatField(blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    preview = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
