"""
Configuração de URLs para o projeto loja_de_roupas.

A lista `urlpatterns` roteia (direciona) URLs para views (visualizações/funções). Para mais informações, consulte:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Exemplos:
Views baseadas em função (Function views)
    1. Adicione um import: from minha_app import views
    2. Adicione uma URL a urlpatterns: path('', views.home, name='home')
Views baseadas em classe (Class-based views)
    1. Adicione um import: from outra_app.views import Home
    2. Adicione uma URL a urlpatterns: path('', Home.as_view(), name='home')
Incluindo outro arquivo de configuração de URL (URLconf)
    1. Importe a função include(): from django.urls import include, path
    2. Adicione uma URL a urlpatterns: path('blog/', include('blog.urls'))
"""

# Importa o módulo de administração padrão do Django
from django.contrib import admin 
# Importa as funções path (para definir rotas) e include (para incluir rotas de outras apps)
from django.urls import path,include 

# Lista de padrões de URL (URLs que o seu projeto reconhece)
urlpatterns = [
    # Mapeia o endereço '/admin/' para a interface de administração do Django.
    path('admin/', admin.site.urls),

    # Mapeia a URL raiz (vazia, ou seja, 'http://127.0.0.1:8000/') 
    # para incluir todas as rotas definidas no arquivo 'urls.py' da sua app 'estoque'.
    # Isso delega o controle das rotas principais para a aplicação 'estoque'.
    path('', include('estoque.urls')),
]