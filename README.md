![Python](https://img.shields.io/badge/python-3.10-blue)
![MongoDB](https://img.shields.io/badge/MongoDB-NoSQL-green)
![Docker](https://img.shields.io/badge/docker-container-blue)

## 📌 Descrição

Este projeto consiste na utilização do MongoDB para manipulação de dados de uma coleção de alunos, utilizando operações básicas e avançadas diretamente no banco.

O projeto utiliza Docker para subir o MongoDB, Python (PyMongo) apenas para inserção inicial dos dados, e MongoDB Compass para execução das consultas e análise dos resultados.

---

## 🛠️ Tecnologias

- Python 3.10
- MongoDB
- Docker & Docker Compose
- PyMongo
- MongoDB Compass

---

## 🧠 Objetivo

Realizar operações no banco de dados MongoDB:

- Inserção de documentos
- Consultas com filtros
- Atualização de dados
- Remoção de documentos
- Aggregations (média e agrupamento)

---

## ▶️ Como executar o projeto

### 🔧 Pré-requisitos

- Docker instalado
- Python instalado
- MongoDB Compass instalado

---

### 🚀 Passo a passo

docker-compose up -d

pip install -r requirements.txt

python mongo_insert.py

---

## 🔗 Conexão com o banco

mongodb://localhost:27017

Acesse:
escola → alunos

---

## 📊 Consultas realizadas (MongoDB Compass)

### 1. Buscar todos os alunos
{}

### 2. Buscar alunos do curso ADS
{ "curso": "ADS" }

### 3. Buscar alunos com idade maior que 21
{ "idade": { "$gt": 21 } }

### 4. Atualizar a idade de um aluno
# Editar o documento manualmente no MongoDB Compass

### 5. Adicionar uma nova nota
# Editar o array "notas" adicionando um novo valor

### 6. Remover um aluno
# Utilizar a opção de delete no MongoDB Compass

### 7. Média de notas por aluno (Aggregation)

[
  {
    "$project": {
      "nome": 1,
      "media": { "$avg": "$notas" }
    }
  }
]

### 8. Quantidade de alunos por curso (Aggregation)

[
  {
    "$group": {
      "_id": "$curso",
      "quantidade": { "$sum": 1 }
    }
  }
]

---

## 📸 Prints

- Prints realizados no MongoDB Compass
- Mostrar filtros, pipelines e resultados

---

## 🐳 Docker

- MongoDB rodando na porta 27017

---

## ⚠️ Observações

- Python utilizado apenas para inserção inicial
- Consultas feitas no MongoDB Compass
- Projeto com foco educacional

---

## 🚀 Melhorias futuras

- Autenticação no MongoDB
- Automatização de consultas
- Interface de visualização
- Deploy em cloud

---

## 👨‍💻 Autor

Desenvolvido por Cairo 🚀