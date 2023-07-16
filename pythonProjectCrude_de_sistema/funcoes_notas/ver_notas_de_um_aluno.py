import json

def ver_notas_de_um_aluno(alunos,notas):
    id = input("Qual ID: ")
    for aluno in alunos:
        if aluno['id'] == id:
            print(aluno)

    for nota in notas:
        if nota['id_de_aluno'] == id:

            print(nota)

def ver_notas_de_um_aluno_da_base_de_dados():
    with open('./base_de_dados.json', 'r') as db:
        dict_db = json.load(db)
        ver_notas_de_um_aluno(dict_db['alunos'],dict_db['notas'])