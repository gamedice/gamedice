from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/', blank=True)
    contain = models.TextField(max_length=3000)
    time_created = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1500)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комметарий'
        verbose_name_plural = 'Комметарии'
