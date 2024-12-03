from django.db import models

# Create your models here.

class Sun(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя солнышка')

    def __str__(self):
        return self.name