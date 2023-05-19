from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/users', blank=True)
    like = models.ForeignKey('Favorites', on_delete=models.CASCADE, blank=True, null=True)

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

class Games(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/', blank=True)
    subscribe = models.TextField()
    date_created = models.DateField()
    rating = models.FloatField()
    count_player = models.FloatField()
    preview = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

class Favorites(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)