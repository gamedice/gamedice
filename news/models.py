from django.db import models
from django.contrib.auth.models import User


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
