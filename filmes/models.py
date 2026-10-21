from django.db import models


class Generos(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Filmes(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    ano_lancamento = models.IntegerField()
    genero = models.ForeignKey(
        Generos,
        on_delete=models.PROTECT,
        related_name='filmes'
    )
    duracao = models.IntegerField()

    def __str__(self):
        return self.titulo
