import json
def remover_aluno(alunos: list):

    id = input("Qual ID: ")
    for aluno in alunos:
        if aluno['id'] == id:
            alunos.remove(aluno)

def remover_aluno_da_base_de_dados():
    dict_db = {}
    with open('./base_de_dados.json','r') as db:
        dict_db = json.load(db)

        with open('./base_de_dados.json', 'w') as db:
            try:
                remover_aluno(dict_db['alunos'])
                json.dump(dict_db,db)
            except Exception:
                json.dump(dict_db,db)