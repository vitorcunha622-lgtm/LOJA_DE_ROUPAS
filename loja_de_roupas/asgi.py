"""
Configuração ASGI (Asynchronous Server Gateway Interface) para o projeto loja_de_roupas.

Este arquivo expõe o "callable" ASGI como uma variável de nível de módulo chamada ``application``.
(O "callable" é a função que o servidor assíncrono chama para iniciar o Django).

Para mais informações sobre este arquivo, consulte
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os # Importa o módulo para interagir com o sistema operacional

# Importa a função padrão do Django para obter o aplicativo ASGI
from django.core.asgi import get_asgi_application

# Define a variável de ambiente que informa ao Django qual arquivo de configurações (settings) usar.
# Ele aponta para 'loja_de_roupas.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loja_de_roupas.settings')

# Esta é a função principal que o servidor ASGI (como Daphne ou Uvicorn) irá chamar.
# Ela carrega o projeto Django e o expõe ao servidor, permitindo a comunicação assíncrona.
application = get_asgi_application()