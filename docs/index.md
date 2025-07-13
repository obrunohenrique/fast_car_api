# 🚗 Fast Car API

API desenvolvida com **FastAPI** para gerenciamento de carros.

## 📦 Sobre o Projeto

O Fast Car API é um projeto backend com o objetivo de oferecer uma API RESTful para criar, consultar, atualizar e excluir informações de veículos. Foi desenvolvido utilizando:

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLModel](https://sqlmodel.tiangolo.com/)
- SQLite como banco de dados
- Taskipy para automatização de tarefas
- Ruff para lint e formatação

## 🛠️ Instalação

Clone o repositório:

```bash
git clone https://github.com/obrunohenrique/fast-car-api.git
cd fast-car-api
```

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate   # Windows
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## 🚀 Executando a aplicação

Execute o servidor com:

```bash
task run
```

A aplicação estará disponível em:

```
http://127.0.0.1:8000
```

Documentação automática disponível em:

- Swagger UI: `/docs`
- Redoc: `/redoc`

---

## 📂 Estrutura do Projeto

```text
fast_car_api/
├── app.py               # Arquivo principal
├── database.py          # Sessão e engine do banco
├── models.py            # Modelos do SQLModel
├── schemas.py           # Schemas (Pydantic)
├── routes.py            # Todas as rotas da API
├── __init__.py
alembic/                 # Migrações do banco
pyproject.toml           # Configurações do projeto
README.md                # Este arquivo
```

---

## 🔧 Comandos de Desenvolvimento

Os seguintes comandos estão definidos no `pyproject.toml` com Taskipy:

| Comando      | Descrição                              |
|--------------|-----------------------------------------|
| `task lint`      | Roda o linter com Ruff                   |
| `task lint_fix`  | Corrige automaticamente os erros de lint |
| `task format`    | Formata o código com Ruff                |
| `task run`       | Executa a aplicação FastAPI              |

---

## 📑 Endpoints Disponíveis

Todas as rotas estão sob o prefixo `/api/v1/cars`:

| Método | Rota        | Descrição                          |
|--------|-------------|------------------------------------|
| POST   | `/`         | Criar um novo carro                |
| GET    | `/`         | Listar todos os carros             |
| GET    | `/{car_id}` | Buscar um carro por ID             |
| PUT    | `/{car_id}` | Atualizar completamente um carro  |
| PATCH  | `/{car_id}` | Atualização parcial de um carro   |
| DELETE | `/{car_id}` | Remover um carro                   |

---

## 📃 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## 👨‍💻 Autor

Desenvolvido por **BrunoH**.
