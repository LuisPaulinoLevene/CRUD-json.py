import json

def remover_notas_de_aluno(alunos,notas):
    id = input("Qual ID: ")
    for aluno in alunos:
        if aluno['id'] == id:
            print(aluno)
    for nota in notas:
        if nota['id_de_aluno'] == id:
            notas.remove(nota)


def remover_notas_de_aluno_da_base_de_dados():
    dict_db = {}
    with open('./base_de_dados.json','r') as db:
        dict_db = json.load(db)

        with open('./base_de_dados.json', 'w') as db:
            try:
                remover_notas_de_aluno(dict_db['alunos'],dict_db['notas'])
                json.dump(dict_db,db)
            except Exception:
                json.dump(dict_db,db)