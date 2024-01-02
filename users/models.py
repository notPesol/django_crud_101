from django.db import models

from django.utils import timezone

# Create your models here.

class User(models.Model):
    username = models.CharField(null = False, unique = True)
    password = models.CharField(null = False)
    created_at = models.DateTimeField(default = timezone.now)
    updated_at = models.DateTimeField(default = timezone.now)
    
    def __str__(self) -> str:
        return self.username