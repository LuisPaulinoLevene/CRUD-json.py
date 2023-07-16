import json

def atualizar_notas_de_aluno(alunos, notas):
    id = input("Qual ID: ")
    for aluno in alunos:
        if aluno['id'] == id:
            print(aluno)
    for nota in notas:
        if nota['id_de_aluno'] == id:

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
                print('Erro. digita um numero decimal separado com ponto, como exe4wreszfdmplo:', nota3)
            media = (nota1 + nota2 + nota3) / 3
            estado = ''
            if media >= 14:
                estado = 'Dispensou'
            elif media >= 10:
                estado = 'Passou'
            else:
                estado = 'Reprovou'
            print(['nota1: ',nota1, 'nota2: ',nota2, 'nota3: ',nota3], '\nMedia:', media, '\nEstado:',estado)

            nota['nota1'] = nota1 if nota1 != '' else nota['nota1']
            nota['nota2'] = nota2 if nota2 != '' else nota['nota2']
            nota['nota3'] = nota3 if nota3 != '' else nota['nota3']
            nota['media'] = media if media != '' else nota['media']
            nota['estado'] = estado if estado != '' else nota['estado']
            print()
            break

def atualizar_notas_de_um_aluno_na_base_de_dados():
    dict_db = {}
    with open('./base_de_dados.json','r') as db:
        dict_db = json.load(db)

        with open('./base_de_dados.json', 'w') as db:
            try:
                atualizar_notas_de_aluno(dict_db['alunos'],dict_db['notas'])
                json.dump(dict_db,db)
            except Exception:
                json.dump(dict_db,db)