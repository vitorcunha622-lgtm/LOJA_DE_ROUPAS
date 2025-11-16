from django.contrib import admin # Importa o módulo de administração do Django

# Importa o seu modelo de dados Produto
from .models import Produto

# Opção 1: O registro mais simples
# admin.site.register(Produto) 
# Esta é a forma mais básica. Registra o modelo, mas usa a visualização padrão do Django.

# Opção 2: O registro recomendado (com personalização do painel)
# Usa o decorador @admin.register(Produto) para registrar a classe de configuração (ProdutoAdmin)
# com o modelo Produto.
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    # Campos que serão mostrados como colunas na lista de produtos no painel Admin.
    # Isso torna a listagem muito mais informativa.
    list_display = ('nome', 'preco', 'estoque', 'descricao_curta')
    
    # Adiciona uma barra lateral para filtros rápidos. 
    # Permite filtrar a lista rapidamente pelo campo 'estoque'.
    list_filter = ('estoque',)
    
    # Adiciona um campo de busca no topo da lista. 
    # O Django irá pesquisar os valores digitados nos campos 'nome' e 'descricao'.
    search_fields = ('nome', 'descricao')
    
    # Campo que define a ordem padrão da listagem.
    # Os produtos serão listados em ordem crescente de 'preco'.
    ordering = ('preco',)

    # Método personalizado para exibir uma versão curta da descrição na lista.
    # Isso evita que descrições longas estiquem demais a tabela.
    def descricao_curta(self, obj):
        # Retorna os primeiros 50 caracteres da descrição seguidos de '...'
        return obj.descricao[:50] + '...' if obj.descricao else ''
    
    # Define o nome amigável para esta coluna personalizada no cabeçalho da lista.
    descricao_curta.short_description = 'Descrição'