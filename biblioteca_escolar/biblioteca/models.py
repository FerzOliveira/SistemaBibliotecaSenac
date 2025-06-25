from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Autor(models.Model):
    nome = models.CharField(max_length=200)
    biografia = models.TextField(blank=True)

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.ManyToManyField(Autor)
    genero = models.CharField(max_length=50, choices=[
        ('ficcao', 'Ficção'),
        ('nao_ficcao', "Não Ficção"),
        ('infantil', 'Infantil'),
        ('academico', 'Acadêmico')
    ])
    quantidade = models.PositiveIntegerField(default=1)
    capa = models.ImageField(upload_to='capas/', blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    def esta_disponivel(self):
        return self.quantidade > 0
    
class Emprestimo(models.Model):

Class Reserva(models.Model):
