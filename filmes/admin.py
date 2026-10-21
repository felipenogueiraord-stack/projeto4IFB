from django.contrib import admin
from .models import Generos, Filmes
from rest_framework.authtoken.models import Token


@admin.register(Generos)
class GenerosAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']


@admin.register(Filmes)
class FilmeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'titulo',
        'ano_lancamento',
        'genero',
        'duracao',
    ]
    search_fields = ['titulo', 'descricao']
    list_filter = ['ano_lancamento', 'genero']


admin.site.register(Token)
