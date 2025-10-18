git clone [https://github.com/vitorcunha622-lgtm/loja-de-roupa.git](https://github.com/vitorcunha622-lgtm/loja-de-roupa.git)
cd LOJA_DE_ROUPAS

🚀 Template README.md para Projeto Django
Markdown

# 🛍️ [Nome do Projeto]: CRUD de Loja de Roupas

## 📋 Sobre o Projeto

Este projeto é um sistema de gerenciamento (CRUD) de backend construído com Django, focado na gestão de produtos, clientes e pedidos para uma loja de roupas.

O objetivo principal é oferecer uma interface administrativa robusta e eficiente para a equipe gerenciar o estoque (criar, ler, atualizar e deletar produtos) e visualizar informações de vendas.

### ✨ Funcionalidades (CRUD)

- **C**reate (Criar): Adicionar novos produtos (nome, preço, estoque, descrição).
- **R**ead (Ler): Visualizar listas de produtos e detalhes individuais.
- **U**pdate (Atualizar): Modificar informações de produtos e estoque.
- **D**elete (Excluir): Remover produtos do catálogo.

## 💻 Tecnologias Utilizadas

| Ferramenta | Descrição |
| :--- | :--- |
| **Python** | Linguagem de programação principal. |
| **Django** | Framework Web para o desenvolvimento do Backend. |
| **SQLite3** | Banco de dados padrão utilizado em desenvolvimento. |
| **pip** | Gerenciador de pacotes Python. |
| **Venv** | Ferramenta para isolamento do ambiente virtual. |

## ⚙️ Como Executar o Projeto Localmente

Siga estas instruções para configurar e rodar o projeto em sua máquina.

### Pré-requisitos

Você precisa ter o **Python** (versão 3.x) e o **Git** instalados em seu sistema.

### 1. Clonar o Repositório

Abra seu terminal e navegue até o diretório onde deseja salvar o projeto:

```bash
git clone [https://github.com/vitorcunha622-lgtm/loja-de-roupa.git](https://github.com/vitorcunha622-lgtm/loja-de-roupa.git)
cd LOJA_DE_ROUPAS
2. Configurar o Ambiente Virtual (VENV)
Crie e ative o ambiente virtual para isolar as dependências:

Bash

# Cria o ambiente virtual
python -m venv venv

# Ativa o ambiente virtual (Windows)
.\venv\Scripts\activate

# Ativa o ambiente virtual (Linux/macOS)
# source venv/bin/activate
3. Instalar as Dependências
Com o ambiente ativado, instale todas as bibliotecas listadas no requirements.txt:

Bash

(venv) pip install -r requirements.txt
4. Rodar o Projeto
Aplique as migrações do banco de dados e inicie o servidor local:

Bash

(venv) python manage.py migrate
(venv) python manage.py runserver
O projeto estará acessível em: http://127.0.0.1:8000/

👤 Autor(es)
[Victor] - @SeuUsuarioNoGitHub

[Rhuan] - @Colega1