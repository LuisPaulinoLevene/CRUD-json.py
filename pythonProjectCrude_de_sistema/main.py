from funcoes_alunos import cadastrar_aluno
from funcoes_alunos import ver_todos_alunos
from funcoes_alunos import ver_um_aluno
from funcoes_alunos import remover_aluno
from funcoes_alunos import atualizar_aluno
from funcoes_notas import lancar_notas_de_um_aluno
from funcoes_notas import ver_notas_de_todos_alunos
from funcoes_notas import ver_notas_de_um_aluno
from funcoes_notas import atualizar_notas_de_aluno
from funcoes_notas import remover_notas_de_aluno

print('\nBEM VINDO AO SISTEMA DE GESTAO DE ALUNOS')

def ciclo_aluno():
    while True:
        print("""Escolha a sua opcao: 
                    1 - Cadastrar aluno
                    2 - Ver todos alunos
                    3 - Ver um aluno
                    4 - Atualizar um aluno
                    5 - Remover um aluno
                    0 - Voltar
              """)
        entrada = input("Escolha a sua opcao:  ")

        if entrada == "1":
            cadastrar_aluno.criar_base_de_dados()
        elif entrada == "2":
            ver_todos_alunos.ver_alunos_da_base_de_dados()
        elif entrada == '3':
            ver_um_aluno.ver_alunos_da_base_de_dados()
        elif entrada == '4':
            atualizar_aluno.atualizar_aluno_na_base_de_dados()
        elif entrada == '5':
            remover_aluno.remover_aluno_da_base_de_dados()
        elif entrada == '0':
            break

def ciclo_notas():
    while True:
        print("""Escolha a sua opcao: 
                    1 - lancar notas
                    2 - Ver notas de todos alunos
                    3 - Ver notas de um aluno
                    4 - Atualizar notas de um aluno
                    5 - Remover notas de um aluno
                    0 - Voltar
              """)
        entrada = input("Escolha a sua opcao: ")

        if entrada == "1":
            lancar_notas_de_um_aluno.lancar_notas_base_de_dados()
        elif entrada == "2":
            ver_notas_de_todos_alunos.ver_notas_de_todos_alunos_da_base_de_dados()
        elif entrada == '3':
            ver_notas_de_um_aluno.ver_notas_de_um_aluno_da_base_de_dados()
        elif entrada == '4':
            atualizar_notas_de_aluno.atualizar_notas_de_um_aluno_na_base_de_dados()
        elif entrada == "5":
            remover_notas_de_aluno.remover_notas_de_aluno_da_base_de_dados()
        elif entrada == "0":
            break

while True:

    print("""
        1 - Gerir alunos
        2 - Gerir Notas
        0 - Sair
          """)
    entrada = input("Escolha a sua opcao: ")
    if entrada == "1":
        ciclo_aluno()
    elif entrada == '2':
        ciclo_notas()
    elif entrada == '0':
        break