import json

def lancar_notas_de_um_aluno(alunos,notas):
    id = input("Qual ID: ")
    for aluno in alunos:
        if aluno['id'] == id:
            print(aluno)

    nota1 = input('nota1: ')
    try:
        nota1 = float(nota1)
    except ValueError:
        nota1 = 0.0
        print('Erro. digita um numero decimal separado com ponto, como exemplo:', nota1)

    nota2 = input('nota2: ')
    try:
        nota2 = float(nota2)
    except ValueError:
        nota2 = 0.0
        print('Erro. digita um numero decimal separado com ponto, como exemplo:', nota2)

    nota3 = input('nota3: ')
    try:
        nota3 = float(nota3)
    except ValueError:
        nota3 = 0.0
        print('Erro. digita um numero decimal separado com ponto, como exemplo:', nota3)
    media = (nota1 + nota2 + nota3) / 3
    estado = ''
    if media >= 14:
        estado = 'Dispensou'
    elif media >= 10:
        estado = 'Passou'
    else:
        estado = 'Reprovou'
    print(['nota1: ', nota1, 'nota2: ', nota2, 'nota3: ', nota3], '\nMedia:', media, '\nEstado:', estado)
    nota_de_aluno = {
        'id_de_aluno': id,
        'nota1': nota1,
        'nota2': nota2,
        'nota3': nota3,
        'media': media,
        'estado': estado
        }
    notas.append(nota_de_aluno)
def lancar_notas_base_de_dados():
    dict_db = {}
    with open('./base_de_dados.json', 'r') as db:
        dict_db = json.load(db)
        with open('./base_de_dados.json', 'w') as db:
            try:
                lancar_notas_de_um_aluno(dict_db['alunos'], dict_db['notas'])
                json.dump(dict_db, db)
            except Exception as _:
                json.dump(dict_db, db)
