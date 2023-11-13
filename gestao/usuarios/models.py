from django.db import models

# Create your models here.
class Usuario(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=64)
    
    def __str__(self) -> str:
        return self.username