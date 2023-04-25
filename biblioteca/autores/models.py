from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length=200)
    nacionalidade = models.CharField(max_length=200)

    def __str__(self):
        return self.nome



