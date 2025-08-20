# from unittest import case
#
#
# def filtrar_filmes(filmes: list, filtro: str, tipo_filtro: str) -> list:
#     filmes_filtrados = []
#     match tipo_filtro:
#         case 'Ano':
#             for filme in filmes:
#                 if filme['Ano'] == filtro:
#                     filmes_filtrados.append(filme)
#
#         case 'Genero':
#             for filme in filmes:
#                 if filme['Genero'] == filtro:
#                     filmes_filtrados.append(filmes)
#         case _:
#             return []
#     return filmes_filtrados
#
#
# filmes = [{'nome': "carros", 'Genero': 'suspense', 'Ano': '2006'},
#           {'nome': "carros 2", 'Genero': 'comedia', 'Ano': '2011'},
#           {'nome': "carros 3", 'Genero': 'drama', 'Ano': '2015'}, ]
#
# filmes = filtrar_filmes(filmes, '2006', 'Ano')
# print(filmes)
#
#
# def votação():
#     candidatos = [0, 0, 0]
#     while True:
#         voto = input('digite em quem voce quer votar para mais gay \n 1 - victor \n 2 - rapha \n 3 - felipe macho alfa \n ou sair\n')
#         if voto == 'sair':
#             break
#         if voto.isdigit():
#             voto = int(voto) - 1
#             if 0 <= voto <= len(candidatos):
#                 candidatos[voto] += 1
#         else:
#             print('resposta invalida')
#     else:
#         print('resposta invalida')
#     for votos in candidatos:
#         print(votos)
#
#
# votação()
#
#
#
#
# tarefas = [{'tarefa': 'lavar a louça' , 'prioridade': 'maxima', 'concluida': True},
#            {'tarefa': 'comprar comida', 'prioridade': 'media', 'concluida': False}]
#
#
#
# # sair
#
#
#
#
#
#
#
#
#
#
#
#
# opcao = 1
# contatos = []
# while opcao != 0:
#     opcao = int(input("""
#     Digite uma opção:
#     1 - Listar Contatos.
#     2 - Adicionar Contato.
#     3 - Editar um Contato.
#     4 - Excluir um contato
#     """))
#
#     match opcao:
#         case 1:
#             for c in contatos:
#                 print("Nome", c['nome'])
#                 print("Telefone:", c['telefone'])
#
#
#         case 2:
#             nome = input('Digite o nome do contato que voce deseja adicionar: ')
#             telefone = input("Digite o telefone do contato")
#             contatos.append({'nome': nome, 'telefone': telefone})
#
#
#         case 3:
#             nome = input('Digite o nome do contato que voce deseja adicionar: ')
#
#             for c in contatos:
#                 if c["nome"] == nome:
#                     telefone = input("digite o novo telefone")
#                     c["telefone"] = telefone
#
#         case 4:
#             nome = input("digite o nomedo contato que deseja excluir")
# #             for c in contatos:
# #                 if c["nome"] == nome:
# #                     contatos.remove(c)
#
# # matriz = []
# # m = 3
# # n = 3
# #
# # for i in range(m):
# #     matriz.append([])
# #     for coluna in range(n):
# #         matriz[i].append(0)
#
#
# print(matriz)

# matriz = []
# m = 3
# n = 3
#
# for i in range(m):
#     linha = []
#     for j in range(n):
#         linha.append(0)
#         if i == j:
#             linha[j] = 1
#
#     matriz.append(linha)
#
#
# for linha in matriz:
#     print(linha)
#



# matriz = []
# m = 3
# n = 3
#
# for i in range(m):
#     linha = []
#     for j in range(n):
#         linha.append(0)
#
#         if i == j:
#
#             linha[j] = 1
#
#
#     matriz.append(linha)
#
#
# for linha in matriz:
#     print(linha)
#


import random

matriz = []
m = 3
n = 3

for i in range(m):
    matriz.append([])
    for j in range(n):
        matriz[i].append(random.randint(1,10))


soma_matriz = 0

for i in matriz:
    for j in i:
        soma_matriz += j

for i in matriz:
    print(i)

# print(soma_matriz)

# diagonal principal
# count = 0
# for i in matriz:
#     print(i[count])
#     count += 1

# diagonal secundaria
contador = -1
for i in matriz:
    print(i[contador])
    contador -= 1



# matriz transposta
matriz = []
transpo = []

a = 3
b = 3

for i in range(a):
    matriz.append([])
    for j in range(b):
        matriz[i].append(random.randint(1,10))

for linha in matriz:
    print(linha)

for j in range(b):
    transpo.append([])
    for i in range(a):
        transpo[j].append(matriz[i][j])

print("    ")
for linha in transpo:
    print(linha)
