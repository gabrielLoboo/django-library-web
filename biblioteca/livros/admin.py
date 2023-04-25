from django.contrib import admin
from .models import Livro

# Register your models here.

class ExibeLivro(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'ano_publicacao', 'isbn')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_filter = ('ano_publicacao',)
    list_per_page = 3



admin.site.register(Livro, ExibeLivro)

