import json
def ver_um_aluno(alunos: list):

    id = input("Qual ID: ")
    for aluno in alunos:
        if aluno['id'] == id:
            print(aluno)

def ver_alunos_da_base_de_dados():
    with open('./base_de_dados.json', 'r') as db:
        dict_db = json.load(db)
        ver_um_aluno(dict_db['alunos'])