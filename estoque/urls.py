from django.urls import path
# Importa todas as Views baseadas em Classe (CBVs) que foi definiu em views.py

from .views import (
    Lista_de_produtos,                 # VIEW para Listar todos os produtos
    visualização_detalhada_dos_produtos, # VIEW para mostrar um produto específico
    criar_visualizacao,                # VIEW para criar um novo produto (formulário)
    atualizacao_de_produto,            # VIEW para editar um produto existente (formulário)
    deletar_produto,                   # VIEW para excluir um produto
)

# Lista de padrões de URL da aplicação 'estoque'
urlpatterns = [
    # 1. HOME/LISTAGEM DE PRODUTOS (URL VAZIA)
    # Rota: /estoque/
    # Mapeia a URL raiz do app para a View que lista todos os produtos.
    path('', Lista_de_produtos.as_view(), name='lista_produtos'), 
    
    # 2. NOVO PRODUTO (CRIAÇÃO)
    # Rota: /estoque/novo/
    # Mapeia para a View que exibe o formulário de criação de novo produto.
    path('novo/', criar_visualizacao.as_view(), name='criar_produto'),
    
    # 3. URLs que usam o ID (pk) - IMPORTANTE: Sempre vêm depois das URLs estáticas!
    # O '<int:pk>' captura um número inteiro (a chave primária do produto) da URL.
    
    # VISUALIZAÇÃO DETALHADA (LEITURA)
    # Rota: /estoque/1/ ou /estoque/15/
    path('<int:pk>/', visualização_detalhada_dos_produtos.as_view(), name='detalhe_produto'), 
    
    # ATUALIZAÇÃO (EDIÇÃO)
    # Rota: /estoque/1/editar/
    path('<int:pk>/editar/', atualizacao_de_produto.as_view(), name='editar_produto'),
    
    # EXCLUSÃO
    # Rota: /estoque/1/excluir/
    path('<int:pk>/excluir/', deletar_produto.as_view(), name='excluir_produto'),
]
