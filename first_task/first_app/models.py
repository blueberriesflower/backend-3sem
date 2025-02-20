from django.db import models

class MyModel(models.Model): # Для эндпоинтов 2 и 3
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
