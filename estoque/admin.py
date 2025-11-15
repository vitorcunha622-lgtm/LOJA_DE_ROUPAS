from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Produto

# Opção 1: O registro mais simples
# admin.site.register(Produto) 

# Opção 2: O registro recomendado (com personalização do painel)
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    # Campos que serão mostrados na lista de produtos no Admin
    list_display = ('nome', 'preco', 'estoque', 'descricao_curta')
    
    # Adiciona uma barra lateral para filtros rápidos
    list_filter = ('estoque',)
    
    # Adiciona um campo de busca no topo da lista
    search_fields = ('nome', 'descricao')
    
    # Campo que permite ordenar por preço
    ordering = ('preco',)

    # Método para exibir uma versão curta da descrição na lista
    def descricao_curta(self, obj):
        return obj.descricao[:50] + '...' if obj.descricao else ''
    descricao_curta.short_description = 'Descrição'