from django.db import models
from django.contrib.auth.models import User

class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pais = models.CharField(max_length=100)