# 📰 News Aggregator

Um agregador de notícias desenvolvido com **Django** e **NewsAPI**, que permite ao usuário buscar notícias por palavra-chave, fonte e filtrar por data. Também exibe as principais manchetes (Top Headlines) quando não há busca ativa.

## 🚀 Funcionalidades

- 🔍 Pesquisa por palavra-chave.
- 🏢 Filtro por fonte de notícias (ex.: BBC, CNN).
- 📅 Filtro por intervalo de datas (válido quando há busca ou fonte selecionada).
- 📰 Exibição das últimas notícias (Top Headlines).
- 🔄 Paginação dos resultados.
- ⚡ Cache das respostas da API para melhorar desempenho.
- 🎨 Interface limpa e responsiva com CSS customizado.

## 📦 Tecnologias utilizadas

- Python 3
- Django
- Requests (integração com a NewsAPI)
- HTML, CSS (estático)
- Bootstrap (opcional para UI)
- Docker 🐳

## 🔑 Pré-requisitos

- Ter Python 3 instalado
- Ter uma chave de API da [NewsAPI](https://newsapi.org/)

## 🚧 Instalação

1. Clone o repositório:

```
    git clone https://github.com/seu-usuario/news-aggregator.git
    cd news-aggregator
```

## ⚙️ Estrutura do Projeto

    news-aggregator/
    ├── news/
    │   ├── migrations/
    │   ├── static/
    │   │   └── css/
    │   ├── templates/
    │   │   └── news/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── news_aggregator/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── db.sqlite3
    ├── manage.py
    └── README.md

## 🗒️ 2. Criar o arquivo `.env`

```
Crie um arquivo chamado `.env` na raiz do projeto com o seguinte conteúdo:
```

```
env
    POSTGRES_DB=aggregatordb
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    OPENWEATHERMAP_API_KEY=sua_api_key_aqui
    DB_HOST=db
    DB_PORT=5432
```

## 🐳 3. Subir os containers
```
    docker-compose up --build
```
## 🔗 4. Acessar a aplicação
```
    Acesse no navegador: http://localhost:8000
```


## ❗ Observações importantes
```
    O filtro por data funciona apenas quando há uma palavra-chave ou uma fonte selecionada, seguindo as regras da NewsAPI.
    A API possui limites no plano gratuito (100 requisições por dia)
    O cache foi configurado para 15 minutos por página.
```

## 🚀 Próximas melhorias
```
    Listagem dinâmica de fontes a partir do endpoint /sources.

    Adicionar categorias (technology, sports, etc.).

    Implementar autenticação de usuários.

    Salvar artigos como favoritos.

    Deploy na nuvem (Render, Vercel ou PythonAnywhere).
```

## 🤝 Contribuição
```
Sinta-se livre para abrir issues, sugerir melhorias ou enviar pull requests.
```

## 📜 Licença
```
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais informações.
```