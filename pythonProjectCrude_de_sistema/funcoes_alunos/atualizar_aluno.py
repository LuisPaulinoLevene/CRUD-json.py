import json

def atualizar_aluno(alunos):
    id = input("Qual ID: ")
    for aluno in alunos:
        if aluno['id'] == id:
            nome = input('nome: ')
            apelido = input('apelido: ')
            idade = input('idade: ')
            aluno['nome'] = nome if nome !='' else aluno['nome']
            aluno['apelido'] = apelido if apelido !='' else aluno['apelido']
            aluno['idade'] = idade if idade !='' else aluno['idade']
            print(aluno)
            break

def atualizar_aluno_na_base_de_dados():
    dict_db = {}
    with open('./base_de_dados.json','r') as db:
        dict_db = json.load(db)

        with open('./base_de_dados.json', 'w') as db:
            try:
                atualizar_aluno(dict_db['alunos'])
                json.dump(dict_db,db)
            except Exception:
                json.dump(dict_db,db)