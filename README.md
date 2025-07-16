# Tarefa 21.14 — FastAPI com Docker e Poetry

Este projeto demonstra como empacotar uma aplicação FastAPI utilizando Docker, Docker Compose e Poetry para gerenciar dependências. É um ambiente de desenvolvimento replicável e pronto para deployment.

---

## Estrutura do Projeto
```
fastapi-docker-poetry/
├── app/
│ └── main.py # Arquivo principal da aplicação FastAPI
├── Dockerfile # Define a imagem Docker
├── docker-compose.yml # Gerencia o container e o ambiente
├── pyproject.toml # Configuração de dependências (Poetry)
├── poetry.lock # Lockfile gerado automaticamente
├── .env # Variáveis de ambiente (opcional)
└── README.md # Instruções e documentação
```

---

## Pré-requisitos

Antes de executar o projeto, você precisa ter instalado:

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose (V2 ou superior)](https://docs.docker.com/compose/)
- (Opcional) [Poetry](https://python-poetry.org/docs/) — usado apenas durante o desenvolvimento local

---

## Como executar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/teut02/Tarefa-21.14_Backend.git
cd fastapi-docker-poetry
