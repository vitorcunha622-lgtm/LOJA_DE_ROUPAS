# estoque/urls.py (Versão CORRIGIDA e organizada)
from django.urls import path
from .views import (
    Lista_de_produtos,
    visualização_detalhada_dos_produtos,
    criar_visualizacao,
    atualizacao_de_produto,
    deletar_produto,
)

urlpatterns = [
    # 1. HOME/LISTAGEM DE PRODUTOS (URL VAZIA)
    path('', Lista_de_produtos.as_view(), name='lista_produtos'), 
    
    # 2. NOVO PRODUTO
    path('novo/', criar_visualizacao.as_view(), name='criar_produto'),
    
    # 3. URLs que usam o ID (pk) - SEMPRE DEPOIS DA URL VAZIA/ESTÁTICA!
    path('<int:pk>/', visualização_detalhada_dos_produtos.as_view(), name='detalhe_produto'), 
    path('<int:pk>/editar/', atualizacao_de_produto.as_view(), name='editar_produto'),
    path('<int:pk>/excluir/', deletar_produto.as_view(), name='excluir_produto'),
]

