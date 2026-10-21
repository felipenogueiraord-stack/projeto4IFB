# Projeto 4 - API de Filmes

Projeto desenvolvido com Django REST Framework para cadastrar, consultar, editar e excluir filmes e gêneros.

## Tecnologias utilizadas

- Python
- Django
- Django REST Framework
- django-filter
- SQLite

## Endpoints

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/api/filmes/` | Lista os filmes |
| GET | `/api/filmes/{id}/` | Consulta um filme específico |
| POST | `/api/filmes/` | Cadastra um filme |
| PUT | `/api/filmes/{id}/` | Atualiza um filme |
| PATCH | `/api/filmes/{id}/` | Atualiza parte dos dados de um filme |
| DELETE | `/api/filmes/{id}/` | Exclui um filme |
| GET | `/api/generos/` | Lista os gêneros |
| POST | `/api/generos/` | Cadastra um gênero |
| GET | `/api/generos/{id}/` | Consulta um gênero específico |
| POST | `/api/token/` | Gera um token de autenticação |

## Testes realizados

Os testes foram realizados utilizando o `curl.exe` no terminal cmd do VsCode

### 1. Listagem de filmes

**Requisição:**

```cmd
curl.exe http://127.0.0.1:8000/api/filmes/
```

**Resultado obtido:**

```json
[
  {
    "id": 1,
    "titulo": "Interestelar",
    "descricao": "Filme do Cristopher Nolan",
    "ano_lancamento": 2014,
    "duracao": 160,
    "genero": 1
  },
  {
    "id": 2,
    "titulo": "O dia em que a terra parou",
    "descricao": "Filme estrelado por Keanu Reeves",
    "ano_lancamento": 2011,
    "duracao": 155,
    "genero": 1
  },
  {
    "id": 3,
    "titulo": "Indiana Jones and the lost Ark",
    "descricao": "Primeiro filme de Harrison Ford como indiana Jones",
    "ano_lancamento": 1989,
    "duracao": 175,
    "genero": 2
  }
]
```

### 2. Consulta de um filme específico

**Requisição:**

```cmd
curl.exe http://127.0.0.1:8000/api/filmes/1/
```

**Resultado obtido:**

```json
{
  "id": 1,
  "titulo": "Interestelar",
  "descricao": "Filme do Cristopher Nolan",
  "ano_lancamento": 2014,
  "duracao": 160,
  "genero": 1
}
```

### 3. Geração de token de autenticação

**Requisição:**

```cmd
curl.exe -X POST http://127.0.0.1:8000/api/token/ ^
  -H "Content-Type: application/json" ^
  -d "{\"username\":\"FelipeGon1\",\"password\":\"Senha0309\"}"
```

**Resposta esperada:**

```json
{
  "token": "a7f2be97e7d86f89a345c6583321f20522b1ee57"
}
```

O token é gerado a partir das credenciais de um usuário cadastrado. O valor retornado deve ser tratado como informação privada.

## Como executar o projeto

1. Ative o ambiente virtual.
2. Instale as dependências listadas no `requirements.txt`.
3. Execute as migrações do banco de dados.
4. Inicie o servidor Django.

A API estará disponível localmente em:

`http://127.0.0.1:8000/api/`

## Autor

Projeto desenvolvido para fins de estudo.
