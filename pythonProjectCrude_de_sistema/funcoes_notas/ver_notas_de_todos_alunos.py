import json
def ver_notas_de_todos_alunos(alunos,notas):
    for aluno in alunos:
        print('=='*60,'\n',aluno)
        for nota in notas:
            if nota['id_de_aluno'] == aluno['id']:
                print(nota,'\n', '=='*60)
                break

def ver_notas_de_todos_alunos_da_base_de_dados():
    with open('./base_de_dados.json', 'r') as db:
        dict_db = json.load(db)
        ver_notas_de_todos_alunos(dict_db['alunos'],dict_db['notas'])