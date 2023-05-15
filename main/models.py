from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    rating = models.FloatField()
    count_player = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    preview = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    liked = models.JSONField(default=list, blank=True)
    photo = models.ImageField(upload_to='images/users', blank=True)

    def __str__(self):
        return self.user

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Posts(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/', blank=True)
    contain = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class News(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/', blank=True)
    contain = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'