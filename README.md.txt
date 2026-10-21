# Projeto 4 - API de Filmes

Projeto desenvolvido com Django e Django REST Framework para
gerenciamento de filmes e gêneros.

## Tecnologias utilizadas

- Python
- Django
- Django REST Framework
- django-filter
- SQLite
- Git e GitHub

## Funcionalidades

- Cadastro, consulta, edição e exclusão de gêneros.
- Cadastro, consulta, edição e exclusão de filmes.
- Relacionamento entre filmes e gêneros por chave estrangeira.
- Autenticação por token.
- Interface administrativa do Django.
- Filtros por título, ano de lançamento e gênero.

## Estrutura dos dados

### Generos
- id
- nome

### Filmes
- id
- titulo
- descricao
- ano_lancamento
- genero
- duracao

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
cd projeto4
```

### 2. Criar e ativar o ambiente virtual no Windows CMD

```bat
python -m venv venv
venv\Scripts\activate.bat
```

### 3. Instalar as dependências

```bat
pip install django django-filter djangorestframework
```

### 4. Aplicar as migrações

```bat
python manage.py makemigrations
python manage.py migrate
```

### 5. Criar o administrador

```bat
python manage.py createsuperuser
```

### 6. Iniciar o servidor

```bat
python manage.py runserver
```

## Endpoints

- `/admin/` - Administração
- `/api/` - Raiz da API
- `/api/generos/` - Gêneros
- `/api/filmes/` - Filmes
- `/api/token/` - Autenticação por token

## Observação

Este projeto foi desenvolvido para fins educacionais.
