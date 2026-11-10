# 📘 Assignment: FastAPI with SQLite Persistence

## 🎯 Objective

Atualize uma API FastAPI de tarefas para persistir os dados em um banco SQLite local. Você praticará comandos SQL básicos e aprenderá a preservar os dados após reiniciar o servidor usando o módulo `sqlite3` da biblioteca padrão do Python.

## 📝 Tasks

### 🛠️ Criar o Banco e a Tabela de Tarefas

#### Descrição
Parta do código inicial, que já implementa as rotas CRUD com armazenamento em memória. Crie uma conexão SQLite e inicialize uma tabela para armazenar as tarefas.

#### Requisitos
O programa concluído deve:

- Usar o módulo `sqlite3` da biblioteca padrão, sem adicionar uma dependência de ORM.
- Criar o arquivo `tasks.db` localmente e a tabela `tasks` caso ela ainda não exista.
- Definir as colunas `id`, `title`, `description` e `completed`, com tipos e valores padrão apropriados.
- Inicializar o banco automaticamente quando a aplicação iniciar.

### 🛠️ Persistir a Criação e a Listagem

#### Descrição
Substitua o armazenamento em memória das rotas de criação e listagem por comandos SQL que leiam e gravem tarefas no SQLite.

#### Requisitos
O programa concluído deve:

- Fazer `POST /tasks` inserir a tarefa no banco e retornar a tarefa criada com seu identificador.
- Fazer `GET /tasks` consultar e retornar as tarefas armazenadas.
- Usar parâmetros SQL (`?`) para passar valores às consultas, em vez de concatenar texto SQL.
- Manter os dados criados após encerrar e iniciar o servidor novamente.

### 🛠️ Persistir a Consulta, a Atualização e a Remoção

#### Descrição
Adapte as rotas de uma tarefa específica para executar consultas e alterações no banco, mantendo as respostas HTTP definidas pela API.

#### Requisitos
O programa concluído deve:

- Fazer `GET /tasks/{task_id}` consultar a tarefa no SQLite e retornar `404` se ela não existir.
- Fazer `PUT /tasks/{task_id}` atualizar os dados da tarefa e retornar `404` se nenhuma tarefa corresponder ao identificador.
- Fazer `DELETE /tasks/{task_id}` remover a tarefa e retornar `204` quando a remoção for concluída, ou `404` se ela não existir.
- Confirmar pela documentação interativa em `/docs` que as alterações continuam disponíveis após reiniciar o servidor.