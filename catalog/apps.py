from django.apps import AppConfig


<<<<<<<< HEAD:login/apps.py
class LoginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'login'
========
class CatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'
>>>>>>>> main:catalog/apps.py
