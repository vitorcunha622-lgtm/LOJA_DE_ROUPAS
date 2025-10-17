from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    
)

from .models import Produto
from django.urls import reverse_lazy

class Lista_de_produtos(ListView):
    model = Produto
    template_name = 'estoque/produto_list.html'
    context_object_name = 'produtos'

class visualização_detalhada_dos_produtos(DetailView):
    model = Produto
    template_name = 'estoque/produto_detail.html'

class criar_visualizacao(CreateView):
    model = Produto
    template_name = 'estoque/produto_form.html'
    fields = ['nome', 'descricao', 'preco', 'estoque']

class atualizacao_de_produto(UpdateView):
    model = Produto
    template_name = 'estoque/produto_form.html'
    fields = ['nome', 'descricao', 'preco', 'estoque' ]

class deletar_produto(DeleteView):
    model = Produto
    template_name = 'estoque/produto_confirm_delete.html'
    # redirecionar apos a exclusao (lista de produto)
    success_url = reverse_lazy('lista_produtos')



