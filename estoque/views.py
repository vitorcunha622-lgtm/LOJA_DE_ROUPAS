from django.shortcuts import render # Função básica para renderizar templates (não usada nas CBVs abaixo, mas é um import comum)

# Importa as classes genéricas de view que facilitam as operações CRUD (Criar, Ler, Atualizar, Deletar)
from django.views.generic import(
    ListView,      # Usada para listar objetos do banco de dados (READ - Lista)
    DetailView,    # Usada para exibir um único objeto em detalhes (READ - Detalhe)
    CreateView,    # Usada para criar novos objetos (CREATE)
    UpdateView,    # Usada para atualizar objetos existentes (UPDATE)
    DeleteView     # Usada para deletar objetos (DELETE)
)

from .models import Produto # Importa o modelo 'Produto' do seu aplicativo de estoque
from django.urls import reverse_lazy # Importa a função para resolver URLs de forma reversa (útil para redirecionamentos após ações)

# --------------------------------------------------------------------------------------
# 1. VISUALIZAÇÃO DE LISTA (READ - Todos os Produtos)
# --------------------------------------------------------------------------------------
class Lista_de_produtos(ListView):
    # O modelo de banco de dados que será consultado (a tabela 'Produto')
    model = Produto
    # O arquivo HTML que será usado para renderizar a lista de produtos
    template_name = 'estoque/produto_list.html'
    # O nome da variável que conterá a lista de objetos dentro do template ({{ produtos }})
    context_object_name = 'produtos'

# --------------------------------------------------------------------------------------
# 2. VISUALIZAÇÃO DETALHADA (READ - Produto Individual)
# --------------------------------------------------------------------------------------
class visualização_detalhada_dos_produtos(DetailView):
    # O modelo de banco de dados que será consultado (um único Produto)
    model = Produto
    # O arquivo HTML que será usado para renderizar os detalhes do produto
    template_name = 'estoque/produto_detail.html'
    # O objeto será acessível no template como {{ object }} ou {{ produto }}

# --------------------------------------------------------------------------------------
# 3. CRIAÇÃO (CREATE)
# --------------------------------------------------------------------------------------
class criar_visualizacao(CreateView):
    # O modelo que será usado para criar o novo objeto
    model = Produto
    # O arquivo HTML que será usado para renderizar o formulário de criação
    template_name = 'estoque/produto_form.html'
    # Os campos do modelo que serão exibidos no formulário para o usuário preencher
    fields = ['nome', 'descricao', 'preco', 'estoque']
    # Após o sucesso, o Django tentará redirecionar para o método get_absolute_url() do modelo.

# --------------------------------------------------------------------------------------
# 4. ATUALIZAÇÃO (UPDATE)
# --------------------------------------------------------------------------------------
class atualizacao_de_produto(UpdateView):
    # O modelo que será usado para buscar e atualizar o objeto
    model = Produto
    # O arquivo HTML que será usado para renderizar o formulário de atualização (reutiliza o mesmo de criação)
    template_name = 'estoque/produto_form.html'
    # Os campos que podem ser editados no formulário
    fields = ['nome', 'descricao', 'preco', 'estoque']
    # O formulário será pré-preenchido com os dados atuais do produto.

# --------------------------------------------------------------------------------------
# 5. EXCLUSÃO (DELETE)
# --------------------------------------------------------------------------------------
class deletar_produto(DeleteView):
    # O modelo que será usado para identificar e deletar o objeto
    model = Produto
    # O arquivo HTML que será renderizado para confirmar a exclusão
    template_name = 'estoque/produto_confirm_delete.html'
    # Redirecionar após a exclusão (lista de produto). 
    # 'reverse_lazy' garante que a URL seja resolvida apenas no momento em que for realmente necessária.
    success_url = reverse_lazy('lista_produtos')



