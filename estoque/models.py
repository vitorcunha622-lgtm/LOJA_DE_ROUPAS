from django.db import models # Importa o módulo básico para criação de modelos
from django.urls import reverse # Importa a função para criar URLs dinamicamente (útil para redirecionamentos)

# Cria seu modelo de dados. 'Produto' será uma tabela no banco de dados.
class Produto(models.Model):
    
    # Campo para o nome do produto:
    # CharField: Campo de texto de tamanho limitado.
    # max_length=100: Limita o nome a 100 caracteres.
    # verbose_name: Rótulo amigável que será exibido na área administrativa do Django.
    nome = models.CharField(max_length = 100, verbose_name='Nome do produto')

    # Campo para a descrição do produto:
    # TextField: Campo de texto longo (sem limite prático de caracteres).
    # blank=True: Permite que o campo fique vazio no formulário.
    # null=True: Permite que o campo fique vazio (NULL) no banco de dados.
    descricao = models.TextField(blank=True, null=True, verbose_name='descrição')

    # Campo para o preço:
    # DecimalField: Campo numérico de ponto flutuante (ideal para moedas).
    # max_digits=10: Número total máximo de dígitos que o número pode ter (incluindo casas decimais).
    # decimal_places=2: Número de casas decimais permitidas (centavos).
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço (R$)')

    # Campo para o estoque:
    # IntegerField: Campo para números inteiros.
    # default=0: O valor padrão quando um novo produto é criado é zero.
    estoque = models.IntegerField(default=0, verbose_name='Estoque')

    # Método Padrão: Retorna a URL canônica (principal) do objeto.
    # O Django usa isso, por exemplo, para saber para onde redirecionar após a criação ou edição de um objeto (CreateView, UpdateView).
    def get_absolute_url(self):
        # 'reverse' busca a URL nomeada 'detalhe_produto' e passa o ID do objeto (self.id) como argumento.
        return reverse('detalhe_produto', args=[str(self.id)])
    
    # Método Padrão: Define como o objeto deve ser representado como uma string (texto).
    # Essa representação é usada em logs e, principalmente, na interface de administração.
    def __str__(self):
        return f'{self.nome} - R${self.preco}'
    
    # Classe Meta: Define metadados sobre o modelo.
    class Meta:
        # Nome amigável singular do modelo na área de administração.
        verbose_name = 'Produto de Roupa'
        # Nome amigável plural do modelo na área de administração.
        verbose_name_plural = 'Produtos de Roupas'
        # OBS: A classe Meta deve ser escrita com "M" maiúsculo (`class Meta:`)
        # O seu código original estava com 'class meta', o que pode causar erros.