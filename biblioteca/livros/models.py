from django.db import models
from autores.models import Autor

# Create your models here.

class Livro (models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=260)
    descricao = models.TextField()
    paginas = models.IntegerField()
    edicao = models.IntegerField()
    ano_publicacao = models.IntegerField()
    idioma = models.CharField(max_length=20)
    isbn = models.CharField(max_length=20)

    def __str__(self):
        return self.titulo
