# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para gerenciar tarefas usando o framework FastAPI. Você praticará rotas HTTP, validação de dados, códigos de status e operações CRUD.

## 📝 Tasks

### 🛠️ Criar uma Rota de Verificação

#### Descrição
Complete o código inicial para criar uma rota de verificação da API e execute o servidor localmente.

#### Requisitos
O programa concluído deve:

- Instalar as dependências com `python -m pip install fastapi "uvicorn[standard]"`.
- Implementar `GET /health` para retornar `{"status": "ok"}`.
- Iniciar o servidor executando `python starter-code.py`.
- Exibir a documentação interativa do FastAPI em `http://127.0.0.1:8000/docs`.

### 🛠️ Criar e Listar Tarefas

#### Descrição
Defina modelos Pydantic para validar os dados das tarefas e implemente as rotas para criar e listar tarefas. Armazene os dados em memória, sem usar um banco de dados.

#### Requisitos
O programa concluído deve:

- Representar cada tarefa com um identificador, título, descrição e estado de conclusão.
- Exigir um título não vazio e permitir uma descrição opcional.
- Implementar `POST /tasks` para criar uma tarefa com identificador gerado pelo servidor e responder com o código `201`.
- Implementar `GET /tasks` para retornar a lista de tarefas cadastradas.
- Retornar erros de validação quando os dados enviados não atenderem ao modelo.

Exemplo de corpo para criar uma tarefa:

```json
{
  "title": "Estudar FastAPI",
  "description": "Criar minha primeira rota"
}
```

### 🛠️ Consultar, Atualizar e Remover Tarefas

#### Descrição
Adicione as rotas para consultar uma tarefa pelo identificador, substituir seus dados e removê-la da coleção.

#### Requisitos
O programa concluído deve:

- Implementar `GET /tasks/{task_id}` para retornar uma tarefa específica.
- Implementar `PUT /tasks/{task_id}` para atualizar título, descrição e estado de conclusão usando um modelo Pydantic.
- Implementar `DELETE /tasks/{task_id}` e responder com o código `204` quando a tarefa for removida.
- Responder com o código `404` quando uma rota receber um identificador que não existe.
- Confirmar as operações usando a documentação interativa em `/docs`.