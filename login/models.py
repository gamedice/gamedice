from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from catalog.models import *

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/users', blank=True)
    # like = models.ForeignKey('Favorites', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
        ordering = ['user']
        unique_together = ('user', 'game')


    def __str__(self):

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

        return f"{self.user.username}'s favorite game: {self.game.name}"

