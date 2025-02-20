from django.db import models
from django.contrib.auth.models import AbstractUser

class MyModel(models.Model): # Для эндпоинтов 2 и 3
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username