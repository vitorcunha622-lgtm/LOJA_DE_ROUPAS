"""
Configuração WSGI (Web Server Gateway Interface) para o projeto loja_de_roupas.

Este arquivo expõe o "callable" WSGI como uma variável de nível de módulo chamada ``application``.
(O "callable" é a função que o servidor web chama para iniciar o Django).

Para mais informações sobre este arquivo, consulte
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os # Importa o módulo para interagir com o sistema operacional

# Importa a função padrão do Django para obter o aplicativo WSGI
from django.core.wsgi import get_wsgi_application 

# Define a variável de ambiente que informa ao Django qual arquivo de configurações (settings) usar.
# Ele aponta para 'loja_de_roupas.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loja_de_roupas.settings')

# Esta é a função principal que o servidor web (como Gunicorn ou uWSGI) irá chamar.
# Ela carrega o projeto Django e o expõe ao servidor.
application = get_wsgi_application()
