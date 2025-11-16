from django.apps import AppConfig # Importa a classe base para configuração de aplicações


class EstoqueConfig(AppConfig):
    # Define o tipo de campo padrão para chaves primárias (IDs) em todos os modelos desta app.
    # BigAutoField é um número inteiro de 64 bits, usado para garantir que o ID não se esgote em projetos grandes.
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Define o nome canônico (o nome oficial) da sua aplicação, que é 'estoque'.
    # Este nome é usado pelo Django em arquivos de settings, migrações e rotas.
    name = 'estoque'