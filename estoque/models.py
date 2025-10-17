from django.db import models
from django.urls import reverse
# Create your models here.

class Produto(models.Model):
    
    nome = models.CharField(max_length = 100, verbose_name='Nome do produto')

    descricao = models.TextField(blank=True, null=True, verbose_name='descrição')

    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço (R$)')

    estoque = models.IntegerField(default=0, verbose_name='Estoque')

    def get_absolute_url(self):
        return reverse('detalhe_produto', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.nome} - R${self.preco}'
    
    class meta:
        verbose_name = 'Produto de Roupa'
        verbose_name_plural = 'Produtos de Roupas'
