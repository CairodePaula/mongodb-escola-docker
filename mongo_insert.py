from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["escola"]
alunos = db["alunos"]

# Limpa e insere alunos
alunos.delete_many({})

alunos.insert_many([
    {
        "nome": "Cairo Gomes",
        "idade": 20,
        "curso": "ADS",
        "notas": [7, 8, 9],
        "endereco": {"cidade": "Maricá", "estado": "RJ"}
    },
    {
        "nome": "Bruno Lima",
        "idade": 22,
        "curso": "ADS",
        "notas": [8, 9, 10],
        "endereco": {"cidade": "Niterói", "estado": "RJ"}
    },
    {
        "nome": "Pedro Santos",
        "idade": 23,
        "curso": "Engenharia",
        "notas": [6, 7, 8],
        "endereco": {"cidade": "Rio de Janeiro", "estado": "RJ"}
    },
    {
        "nome": "Ana Costa",
        "idade": 21,
        "curso": "Medicina",
        "notas": [9, 9, 10],
        "endereco": {"cidade": "São Gonçalo", "estado": "RJ"}
    },
    {
        "nome": "Lucas Lima",
        "idade": 24,
        "curso": "ADS",
        "notas": [5, 6, 7],
        "endereco": {"cidade": "Itaboraí", "estado": "RJ"}
    }
])

print("Alunos inseridos com sucesso!")