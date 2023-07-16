import json

def cadastrar_aluno(alunos: list):
    nome = input("Nome: ")
    apelido = input("Apelido: ")
    idade = input("Idade: ")
    id = input("ID: ")
    print('Nome:',nome,apelido, '\nidade:',idade, '\nid:', id)

    aluno = {
        "nome": nome,
        "apelido": apelido,
        "idade": idade,
        'id': id
        }

    alunos.append(aluno)

def criar_base_de_dados():
    dict_db = {}
    with open('./base_de_dados.json','r') as db:
        dict_db = json.load(db)

        with open('./base_de_dados.json', 'w') as db:
            try:
                cadastrar_aluno(dict_db['alunos'])
                json.dump(dict_db,db)
            except Exception as _:
                json.dump(dict_db,db)

