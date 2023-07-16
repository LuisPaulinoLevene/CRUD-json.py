import json
def ver_todos_alunos(alunos: list):
    for aluno in alunos:
        print('=='*60, '\n', aluno, '\n','=='*60)

def ver_alunos_da_base_de_dados():
    with open('./base_de_dados.json', 'r') as db:
        dict_db = json.load(db)
        ver_todos_alunos(dict_db['alunos'])