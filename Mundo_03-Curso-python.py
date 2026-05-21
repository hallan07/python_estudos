# teste velocidade dos SOs
# from time import time
# a = time()
# cont = 0
# while cont != 100000000:
#     cont += 1
# print(f'Fim - Tempo: {time() - a:0.4f} segundos')

# 100 milhões média de 5 com Azure jupyter 16,7812
# 100 milhões média de 5 com ubuntu 38,3175 seg (as vezes dá menos 10,6189)
# 100 milhões média de 5 com windows 63,2266 seg
# 50 milhões média de 3 com (iphone 6)iOS 20,249 seg

# Aula 16 - Tuplas
# tuplas são imutáveis

# lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
# for comida in lanche:
#     print(comida)

# for c in range(0, len(lanche)):
#     print(lanche[c], c)

# for pos in enumerate(lanche): # se for utilizado so o enumerate ele trás o indice e o item
#     print(pos)

# for pos, comida in enumerate(lanche): # enumerate faz o indice de cada elemento
#     print(pos, comida)

# a = (2, 4, 5, 6)
# b = (3, 5, 7, 8, 9)
# c = a + b
# print(c)
# print(type(c))
# print('len', len(c))
# print('sorted', sorted(lanche))
# print('cont', c.count(5)) # contar quantas vezes o item aparece na lista
# print('index', c.index(5)) # retorna a posição
# print('index', c.index(5, 1)) # retornar a posição a partir da posição 1

# a tupla só pode ser deletada por inteira pra ser reescrita
# pessoa = ('Gustavo', 35, 'M', 99.88)
# print(pessoa)
# del(pessoa)
# pessoa = ('Jão', 40, 'M', 85.86)

# criei um método para alterar a tupla em lista
# pessoa = ('Jão', 40, 'M', 85.86)

# def tran_lista(tupla):
#     lista = []
#     for x in range(len(tupla)):
#         lista.append(tupla[x])
#     del(tupla)
#     tupla = []
#     for y in lista:
#         tupla.append(y)
#     return tupla
#
# print(tran_lista(pessoa))

# exercício 72

# num = int(input('Digite um número entre 0 e 20: '))
# extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
#            'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quize', 'dezesseis',
#            'dezessete', 'dezoito', 'dezenove', 'vinte')
# print(f'Você digitou o número {extenso[num]}')

# exercício 73

# brasileirao = ('Flamengo', 'Palmeiras', 'Santos', 'Internacional', 'Corinthians',
#                'São Paulo', 'Grêmio', 'Bahia', 'Atlhetico-PR', 'Atlético')
# print(f'Os cinco primeiros colocados do Brasileirão são: \n{brasileirao[:5]}\n'
#       f'Os quatro últimos dentre os dez primeiros são:\n{brasileirao[-4:]}')
# print(f'A ordem alfabética dos dez primeiros é:\n{sorted(brasileirao)}')
# print('A posição do São Paulo na tabela é {}ª colocado.'.format(brasileirao.index("São Paulo") + 1))

# exercício 74
# from random import randint as rd
#
# tupla = rd(1, 10), rd(1, 10), rd(1, 10), rd(1, 10), rd(1, 10)
# print(f'Os valores sorteados foram: {tupla}')
# print(f'O maior é {max(tupla)}')
# print(f'O menor é {min(tupla)}')

# exercício 75

# tupla = int(input('Digite um número: ')), int(input('Digite um número: ')),\
#         int(input('Digite um número: ')), int(input('Digite um número: '))
#
# if 3 in tupla:
#     print(f'O valor 3 está na {tupla.index(3) + 1}ª posição')
# elif 3 not in tupla:
#     print('O valor 3 não foi digitado')
# print(f'A quantidade de números 9 digitados foram: {tupla.count(9)}')
# print('Os números pares digitados foram: ', end='')
# for num in tupla:
#     if num % 2 == 0:
#         print(num, end=' ')

# exercício 76

# materiais = 'Lápis', 1.75,\
#             'Borracha', 2.00,\
#             'Caderno', 15.90,\
#             'Estojo', 25.00,\
#             'Transferidor', 4.20,\
#             'Compasso', 9.99,\
#             'Mochila', 120.32,\
#             'Canetas', 22.30,\
#             'Livro', 34.90
# print('-'*29)
# print(f'{"Listagem de Preços": ^29}')
# print('-'*29)
# for n in range(0, (len(materiais)), 2):
#     print(f'{materiais[n]:.<20}R$ {materiais[n + 1]:>6.2f}')
# print('-'*29)

# exercício 77

# palavras = 'python', 'curso', 'data science', 'esforço', 'aprendizado', 'liberdade'
#
# for pal in palavras:
#     print(f'\nPalavra: {pal.upper()} Vogais: ', end='')
#     for let in pal:
#         if let in 'aeiou':
#             print(let, end=' ')


# Aula 17 - Listas 01
# a = [1, 2, 3, 4, 5]
# b = a[:]
# b[1] = 8
# b.remove(3)
# del b[1]
# b.insert(1, 2)
# b[2] = 3
# b.pop(3)
# b.append(4)
# b.append(5)

# exercicio 78
# lista = []
# for c in range(0, 5):
#     num = int(input(f'Digite o valor para a posição {c}: '))
#     lista.append(num)
# print(f'Você digitou os valore {lista}')
# print(f'O maior valor digitado foi {max(lista)}, na posição {lista.index(max(lista))}')
# print(f'O menor foi o {min(lista)}, na posição {lista.index(min(lista))}')

# exercicio 79
# lista = []
# while True:
#     n = int(input('Digite um valor: '))
#     if n in lista:
#         print('O valor não pode ser duplicado')
#     else:
#         lista.append(n)
#     opc = input('Continuar [s/n]: ').strip().lower()
#     if opc == 'n':
#         break
# lista.sort()
# print(f'Os valores adicionados foram {lista}')

# exercico 80 - ordenam ser usar sort
# n = int(input('Digite um valor: '))
# print(f'Adicionado')
# lista = []
# lista.append(n)
# for c in range(0, 4):
#     n = int(input('Digite um valor: '))
#     cont = 0
#     for num in lista:
#         if n < num:
#             lista.insert(cont, n)
#             print(f'Add na posição {cont}')
#             break
#         elif n > max(lista):
#             lista.insert(len(lista), n)
#             print(f'Add no final da lista')
#             break
#         cont += 1
# print(f'Os valores digitados em ordem foram: {lista}')

# outra forma
# lista = []
# for c in range(0 , 5):
#     n = int(input('Digite um valor: '))
#     if c == 0 or n > lista[-1]:
#         lista.append(n)
#     else:
#         pos = 0
#         while pos < len(lista):
#             if n <= lista[pos]:
#                 lista.insert(pos, n)
#                 break
#             pos += 1
# print(f'Os valores digitados em ordem foram: {lista}')


# exercicio 81
# lista = []
# while True:
#     n = int(input('Digite um valor: '))
#     lista.append(n)
#     opc = input('Continuar [s/n]: ').strip().lower()
#     if opc == 'n':
#         break
# lista.sort(reverse=True)
# print(f'Você digitou {len(lista)} números.')
# print(f'Os valores em ordem decrescente são: {lista}')
# if 5 in lista:
#     print(f'O valor 5 está na posição {lista.index(5)}')
# else:
#     print('O valor 5 não foi digitado')

# exercicio 82

# lis = []
# par = []
# imp = []
# while True:
#     n = int(input('Digite um número: '))
#     lis.append(n)
#     opc = input('Continuar [s/n]: ').strip().lower()
#     if opc == 'n':
#         break
# for n in lis:
#     if n % 2 == 0:
#         par.append(n)
#     else:
#         imp.append(n)
# print(f'Os números adicionados foram: {lis}')
# print(f'Os pares são: {par}')
# print(f'Os ímpares são: {imp}')

# exercicio 83 - Análise de expressão
# exp = input('Insira a expressão: ')
# if exp.count('(') == exp.count(')'):
#     print('A expressão está correta')
# else:
#     print('A expressão está errada!')

# Aula 18 - Listas 02

# exercício 84
# pessoas = []
# pes_kg = lev_kg = 0
# while True:
#     cad = []
#     cad = [input('Nome: '), int(input('Peso: '))]
#     pessoas.append(cad[:])
#     opc = input('Continuar [s/n]: ').strip().lower()
#     if len(pessoas) == 1:
#         pes_kg = lev_kg = cad[1]
#     if opc == 'n':
#         break
# print(f'Foram cadastradas {len(pessoas)} pessoas.')
# pes = []
# lev = []
# for c in range(len(pessoas)):
#     if pessoas[c][1] >= 90:
#         pes.append(pessoas[c][0])
#         if pessoas[c][1] > pes_kg:
#             pes_kg = pessoas[c][1]
#     else:
#         lev.append(pessoas[c][0])
#         if pessoas[c][1] < lev_kg:
#             lev_kg = pessoas[c][1]
# print(f'O maior peso foi {pes_kg} Kg')
# print(f'Pessoas mais pesadas foram {pes}')
# print(f'O menor peso foi {lev_kg} Kg')
# print(f'Pessoas mais leves foram {lev}')

# exercicio 85
# par = []
# imp = []
# for c in range(0 , 5):
#     n = int(input('Digite um número: '))
#     if n % 2 == 0:
#         par.append(n)
#     else:
#         imp.append(n)
# total = []
# par.sort()
# imp.sort()
# total.append(par)
# total.append(imp)
# print(f'OS números pares foram: {par}\nOs ímpares foram: {imp}')
# print(f'O total de números são: {total}')

# exercicio 86 - Matriz

# lin1 = [int(input('Valor para [linha 01]: ')), int(input('Valor para [linha 01]: ')),
#     int(input('Valor para [linha 01]: '))]
#
# lin2 = [int(input('Valor para [linha 02]: ')), int(input('Valor para [linha 02]: ')),
#     int(input('Valor para [linha 02]: '))]
#
# lin3 = [int(input('Valor para [linha 03]: ')), int(input('Valor para [linha 03]: ')),
#     int(input('Valor para [linha 03]: '))]
#
# print('linha 01', lin1,
#       '\nlinha 02', lin2,
#       '\nlinha 03', lin3)

# outra forma, mais correta
# t_mat = 3
# matriz = []
# for i in range(0, t_mat):
#     lin = []
#     for x in range(0, t_mat):
#         l = int(input(f'Digite um valor para [{i}, {x}]:'))
#         lin.append(l)
#     matriz.append(lin[:])
# del lin, l
# for i in range(0, t_mat):
#     for x in range(0, t_mat):
#         print(f'[ {matriz[i][x]} ]', end='')
#         if x == (t_mat - 1):
#             print('\n', end='')
# del i, x, t_mat

# outra forma, por colunas
# t_mat = 3
# matriz = []
# for y in range(0 , t_mat):
#     col = []
#     for x in range(0, t_mat):
#         n = int(input(f'Digite um número para [{y}, {x}]: '))
#         col.append(n)
#     matriz.append(col)
# del n, col
# for y in range(0, t_mat):
#     for x in range(0, t_mat):
#         print(f'[ {matriz[x][y]} ]', end='')  # inverter o y e x no fatiamento
#         if x == (t_mat - 1):                  # pata obter uma matrizpor colunas
#             print('\n', end='')
# del y, x, t_mat

# outra forma mais simples, por coluna
# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for y in range(0, 3):
#     for x in range(0, 3):
#         matriz[y][x] = int(input(f'Digite um valor. Coluna {y} Linha {x}: '))
# print('---'*7)
# for x in range(0, 3):
#     for y in range(0, 3):
#         print(f'[{matriz[y][x]:^5}]', end='')
#     print()

# exercicio 87 - Matriz aprimorada
# t_mat = int(input('Tamanho da matriz[TxT]: '))
# print(f'Matriz {t_mat} x {t_mat}')
# soma_par = 0
# matriz = []
# for y in range(0, t_mat):
#     col = []
#     for x in range(0, t_mat):
#         n = int(input(f'Digite um número para [col {y}, lin {x}]: '))
#         if n % 2 == 0:
#             soma_par += n
#         col.append(n)
#     matriz.append(col)
#
# print(f' Matriz {t_mat} x {t_mat} ')
# soma_ter = 0
# maior_seg = 0
# for x in range(0, t_mat):  # inverter o y e x no for, altera de linha para coluna
#     for y in range(0, t_mat):
#         print(f'[{matriz[y][x]:^5}]', end='')
#         if y == (t_mat - 1):
#             print('\n', end='')
#         if y == 2:  # soma da terceira coluna
#             soma_ter += matriz[y][x]
#         if x == 1:  # maior valor para a segunda linha
#             if matriz[y][x] > maior_seg:
#                 maior_seg = matriz[y][x]
#
# print(f'A soma de todos números pares é {soma_par}')
# print(f'A soma da terceira coluna é {soma_ter}')
# print(f'O maior valor da segunda linha é {maior_seg}')
#
# del y, x, t_mat, n, col

# Exercício 88 - Mega Sena
# from random import randint as rd
# from time import sleep as sl
#
# n = int(input('Quantos jogos quer gerar: '))
# for c in range(0, n):
#     jogo = [rd(1, 60), rd(1, 60), rd(1, 60),
#             rd(1, 60), rd(1, 60), rd(1, 60)]
#     print(f'Jogo {c + 1}:', jogo)
#     sl(0.4)

# outra forma
# from random import randint as rd
# from time import sleep as sl
# ten = 0
# n = int(input('Quantos jogos quer gerar: ')) * 6
# lista = []
# jogo = []
# while len(lista) < n:
#     s = rd(1, 60)
#     ten += 1
#     if s not in lista:
#         lista.append(s)
# i = 0
# f = 6
# cont = 0
# lista.sort()
# while cont < (n / 6):
#     print(lista[i:f])
#     i += 6
#     f += 6
#     cont += 1
#     sl(0.4)
# print(f'Tantavas: {ten} para gerar {n} números')

# # exercício 89 - cadastro alunos notas
# cadastro = []
# while True:
#     nome = input('Nome: ')
#     nota1 = float(input('Nota 01: '))
#     nota2 = float(input('Nota 02: '))
#     med = (nota1 + nota2) / 2
#     cadastro.append([nome, [nota1, nota2], med])
#     opc = input('Continuar [s/n]: ').strip().lower()
#     if opc == 'n':
#         break
# print('--'*13)
# print(f'{"No.":<4}{"Nome":<11}{"Média":<}')
# print('--'*13)
# for n, c in enumerate(cadastro):
#     print(f'{n:<4}{c[0]:<11}{c[2]:>.2f}')
# print('--'*13)
#
# while True:
#     opc = int(input('Mostrar nota de qual aluno? (999 fecha) '))
#     if opc == 999:
#         break
#     else:
#         print(f'As notas de {cadastro[opc][0]} são: {cadastro[opc][1]}')
#     print('--' * 13)
# print('--'*13)
# print('Programa finalizado.')
# exit()

# Aula - dicionários

# sorted(jog.values())  # ordenar valores
# sorted(jog.keys())  # ordenam chaves


# exercicios 90
# cad = dict()
# cad['nome'] = input('Nome: ')
# cad['nota'] = float(input('Nota: '))
# if cad['nota'] >= 7:
#     cad['situa'] = 'aprovado'
# else:
#     cad['situa'] = 'reprovado'
# print(cad.values())

# Ordenar dicionários
'''Há três formas de ordenar docionparios:
sorted(jogo, key=jogo.get, reverse=True)
dentro de um for para coloc-lo em outra variável organizado
for n, k in enumerate(sorted(jog, key=jog.__getitem__, reverse=True)):
ou from operator import itemgetter
nova_variavel = sorted(dic_para_ordenar.items(), key=itemgetter(1), reverse=True)
se usar (0) ele organiza a chave ese usar (1) os valores,
mas assim vem como lista
'''

# Ordenam valores do dicionário com for retornando a chave
# dicionario = {'nome1': 5, 'nome2': 1, 'nome3': 3, 'nome4': 6, 'nome5': 2}
#
# dic = {}
# for c in sorted(dicionario, key=dicionario.get):  # pode usar reverse=True
#     dic[c] = dicionario[f'{c}']
# dicionario.clear()
# dicionario = dic
# del dic

# Ordenam as chaves
# dic = {}
# for k, v in sorted(dicionario.items()):
#     dic[k] = dicionario[f'{k}']
# dicionario.clear()
# dicionario = dic
# del dic

# mostrar as chaves ordenadas
# for k in sorted(dicionario.keys()):
#     print(k)
# mostrar os valores ordenados
# for v in sorted(dicionario.values()):
#     print(v)

# exercícios 91 - Ordenam valores de um dicionário

# from random import randint as rd
# from time import sleep as sl
#
# jog = {}
# for c in range(1, 5):
#     jog[f'jogador{c}'] = rd(1, 6)
#     print(f"O jogador{c} {jog[f'jogador' + str(c)]}")
#     sl(0.5)
# print('Ranking dos jogadores:')
#
# # Ordenar os valores do dicionário reverse
# dic = {}
# for n, k in enumerate(sorted(jog, key=jog.__getitem__, reverse=True)):
#     dic[f'{k}'] = jog[f'{k}']
#     print(f'{n + 1}ª lugar: {k} com {jog[k]}')
#     sl(0.5)
# jog.clear()
# jog = dic
# del dic

# minha solução menor, sem gravar um novo dic organizado
# from random import randint as rd
# from time import sleep as sl
#
# jog = {}
# for c in range(1, 5):
#     jog[f'jogador{c}'] = rd(1, 6)
#     print(f"     O jogador{c} tirou {jog[f'jogador' + str(c)]}")
#     sl(0.5)
# print(f"{' == Ranking dos jogadores =='}")
# for n, k in enumerate(sorted(jog, key=jog.__getitem__, reverse=True)):
#     print(f'  {n + 1}ª lugar: {k} com {jog[k]}')
#     sl(0.5)

# outra forma enciontrada nos comentários
# from random import randint
# print('Valores sorteados:')
# jogo = dict()
# for k in range(1, 5):
#     j = 'jogador' + str(k)
#     jogo[j] = randint(1, 6)
#     print(f'{j} tirou {jogo[j]} no dado')
# print('-=' * 30)
# print(' ==RANKING DOS JOGADORES == ')
# c = 1
# for k in sorted(jogo, key=jogo.get, reverse=True):
#     print(f'{c}° lugar: {k} tirou {jogo[k]}')
#     c += 1

# exercício 92 - cadastro carteira de trabalho
# from datetime import datetime as dt
#
# cad = {}
# cad['nome'] = input('Nome: ').strip().title()
# cad['nascimento'] = int(input('Ano de nascimento: '))
# cad['idade'] = dt.today().year - cad['nascimento']
# cad['ctps'] = int(input('Nº carteira de trab [0 se não]: '))
# if cad['ctps'] != 0:
#     cad['contratação'] = int(input('Qual o ano de contratação: '))
#     cad['salário'] = float(input('Salário: '))
#     cad['aposentadoria'] = (32 - (dt.today().year - cad['contratação'])) + cad['idade']
# print('--'*20)
# for k, v in cad.items():
#     print(f'{k.capitalize()} = {v}')

# exercicio 93 - aproveitamento jogador

# jogador = {}
# soma = 0
# gols = []
# jogador['nome'] = input('Nome do jogador: ')
# jogador['partidas'] = int(input('Quantas partidas ele jogou: '))
# for c in range(jogador['partidas']):
#     g = int(input(f'Número de gols na partida {c + 1}: '))
#     soma += g
#     gols.append(g)
# jogador['gols'] = gols[:]
# jogador['total'] = soma
# print('--'*20)
# for k, v in jogador.items():
#     print(f'O campo {k.capitalize()} tem o valor {v}.')
# print('--'*20)
# print(f"O jogador {jogador['nome']} jogou {jogador['partidas']} partidas.")
# for n, v in enumerate(jogador['gols']):
#     print(f'Na partida {n + 1}, fez {v} gols.')
# print(f'Com o total de {jogador["total"]} gols.')

# exercio 94 - cadastro e análise demográfica
# cad = {}
# lista = []
# soma = 0
# while True:
#     cad['nome'] = input('Nome: ').strip().capitalize()
#     cad['idade'] = int(input('Idade: '))
#     soma += cad['idade']
#     while True:
#         cad['sexo'] = input('Sexo: ').strip().lower()[0]
#         if cad['sexo'] in 'mf':
#             break
#         print('Erro! Digite apenas "m" para masculino ou "f" para feminino')
#     lista.append(cad.copy())
#     cad.clear()
#     while True:
#         opc = input('Contiuar [s/n]: ').strip().lower()[0]
#         if opc in 'sn':
#             break
#         print('Erro! Digite apenas "s" para sim ou "n" para não.')
#     if opc == 'n':
#         break
#     print('--'*25)
# med = soma / len(lista)
# mina = []
# acima = []
# for n, dic in enumerate(lista):
#     soma += dic['idade']
#     if dic['sexo'] == 'f':
#         mina.append(dic['nome'])
#     if med < dic['idade']:
#         acima.append(n)
# print('--'*20)
# print(f'Foram cadastradas {len(lista)} pessoas.')
# print(f'A média de idade do grupo é {med:.2f} anos.')
# print(f'Mulheres cadastradas: {mina}')
# print(f'Pessoas com idade acima da média:\n')
# for c in acima:
#     print(lista[c])

# exercicio 95 - aproveitamento do jogador aprimorado

# jogador = {}
# gols = []
# tabela = []
# while True:
#     jogador['nome'] = input(' Nome do jogador: ').strip().capitalize()
#     jogador['partidas'] = int(input(' Quantas partidas ele jogou: '))
#     soma = 0
#     for c in range(jogador['partidas']):
#         g = int(input(f' Número de gols na partida {c + 1}: '))
#         soma += g
#         gols.append(g)
#     jogador['total'] = soma
#     jogador['gols'] = gols[:]
#     gols.clear()
#     tabela.append(jogador.copy())
#     jogador.clear()
#     while True:
#         opc = input(' Continuar [s/n]: ').strip().lower()[0]
#         if opc in 'sn':
#             break
#         print('\033[31m Digie "s" para sim e "n" para não.\033[m')
#     if opc == 'n':
#         break
#     print('--' * 25)
#
# print('=='*30)
# print(f' \033[1mCod.  ', end='')
# for i in tabela[0].keys():
#     print(f'{i.capitalize():<15}', end='')
# print('\033[m')
# print('--'*30)
# for n, v in enumerate(tabela):
#     print(f'{n:^6}', end=' ')
#     for d in v.values():
#         print(f'{str(d):<15}', end='')
#     print()
# print('--'*30)
#
# while True:
#     print()
#     opc = int(input(' Mostrar dados de qual jogador(999 fechar): '))
#     print('=='*25)
#     if opc == 999:
#         break
#     if opc >= len(tabela) or opc < 0:
#         print('\033[31m Opção inválida.\033[m')
#     else:
#         print(f"\033[7m {tabela[opc]['nome']} => Partidas: "
#               f"{tabela[opc]['partidas']} Total de gols: "
#               f"{tabela[opc]['total']} \033[m")
#         print('--'*25)
#         for n, v in enumerate(tabela[opc]['gols']):
#             print(f' No jogo {n + 1} fez {v} gols.')
#         print('--'*25)
# print(f'\033[34m Programa finalizado.\033[m')

# Aula 20 - Funções
# def titulo(txt):
#     print('-' * len(txt))
#     print(f'\033[1;7m{txt:^}\033[m')
#     print('-' * len(txt))



# titulo(' -     Python é muito bom     - ')

# def soma(a, b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'Soma {a} + {b} = {s}')
#
# soma(1.2,59)
#
# def cont(* num):
#     tam = len(num)
#     print(f'Input: {num}\nQuantidade: {tam}')
#
# cont(10, 2, 2.5, 6)
#
# def raiz(lst):
#     pos = 0
#     while pos != len(lst):
#         lst[pos] **= 2
#         print(lst[pos])
#         pos += 1
#
# numeros = [2, 5, 4, 5.6, 9]
#
# raiz(numeros)
#
# def soma(* num):
#     s = 0
#     for n in num:
#         s += n
#     print(f'Soma dos valores: {num}\nResultado: {s}')
#
# soma(2, 6, 9, 6.5, 7, 8.6)

# Exercício 96 - área

# def area(a, b):
#     d = a * b
#     print('--' * 11)
#     print(f'A área {a} x {b} = {d:.2f}m')
#     print('--' * 11)
#
# titulo(' Controle de Terrenos ')  # chama a primeir função de titulo
# area(float(input('Largura (m): ')), float(input('Comprimento (m): ')))

# Exercício 97 - linha

# def texto(txt):
#     print(f'-' * (len(txt) + 2))
#     print(f' {txt:^} ')
#     print(f'-' * (len(txt) + 2))

# texto('Qualquer texto escrito aqui e centralizado')
# texto('Texto pequeno')

# Exercício 98 - contagem
# from time import sleep as sl
#
# def contagem(ini, fim, pas):
#     n = 1
#     if pas < 0:
#         pas *= -1
#     titulo(f' Contagem de {ini} até {fim} de {pas} em {pas}. ')
#     if fim <= 0:
#         n = -1
#     if ini > fim:
#         pas *= -1
#     if ini < fim and pas == 0:
#         fim = ini
#         pas = 1
#     if ini > fim and pas == 0:
#         if fim == 0:
#             fim = ini - 1
#         else:
#             fim = ini
#         pas = 1
#     for c in range(ini, fim + n, pas):
#         sl(0.4)
#         print(f' {c} ', end='')
#     print()
#     lin()
#
#
# contagem(1, 10, 1)
# contagem(1, 10, -1)
# contagem(10, 0, 2)
# contagem(10, 0, -2)
# contagem(1, 10, 0)
# contagem(10, 1, 0)
# contagem(0, 1, 0)
# contagem(1, 0, 0)  # erro

# print('Agora é sua vez de personalizar a contagem')
# contagem(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))

# Exercicio 99 - maior contador
# from time import sleep as sl
#
# def maior(* num):
#     titulo(' Analisando os números ')
#     for c in num:
#         print(f' {c} ', end='')
#         sl(0.4)
#     if num == 0:
#         tam = 0
#     else:
#         tam = len(num)
#     print()
#     lin()
#     print(f'Foram informados {tam} números')
#     print(f'O maior é: {max(num)}')
#     lin()
#
#
# maior(1, 2, 3, 5, 9)
#
# maior(5)
#
# maior(0, 0)

# exercício 100 - sorteio e somapar
# from random import randint as rd
# from time import sleep as sl
#
# def sorteio(lst, qtd):
#     titulo(f'Sorteando {qtd} valores para a lista {lst}: ')
#     for r in range(qtd):
#         ram = rd(0, 100)
#         lst.append(ram)
#         print(f'Valor {r + 1}: {ram}')
#         sl(0.4)
#     lin()
#
# def somapar(lst):
#     titulo(f' Somando os valores pares de {lst} ')
#     soma = 0
#     for c in lst:
#         if c % 2 == 0:
#             print(f' {c} ', end='')
#             sl(0.4)
#             soma += c
#     print()
#     lin()
#     print(f'Resultado: {soma}')
#     lin()
#
#
# lista = []
# sorteio(lista, 10)
#
# somapar(lista)

# Aula 21 - Funções parte 2

# DOCSTRINGS

''' Docstrings são manuais que pode ser criados descrevendo a funcionalidade
de qualquer função/método que eu crie. Para outros usuários poderem usar.
É a criação dos docs, que podem se chamdos atravás o comando helo()'''

# Exemplo

# def titulo(txt):
#     """
#     Essa é uma função/método para imprimir um título no terminal,
#     com um formato próprio.
#     :param txt: é o argumento que vai dentro de print, portanto deve-se usar
#     aspas ''.
#     Exemplo 01: titulo('Título que pretento mostar')
#     Exemplo 02: titulo(f'O nome selecionado é {nome}.')
#     :return: não há retorno, é impresso no terminal
#     """
#     print('-' * len(txt))
#     print(f'\033[1;7m{txt:^}\033[m')
#     print('-' * len(txt))
#
#
# def lin():
#     print('---' * 11)

# HELP - AJUDA INTERATIVA

# help(titulo)  # esse é uma forma de acessar o help para qualquer comando
#
# print(titulo.__doc__)  # outra forma, imprime o doc

# também pode ser aberto no terminal com o comando help(), e sair com quit

# PARAMETROS OPCIONAIS

'''Abaio uma função que aceita somente 03 parâmetros (a, b, c)
Se caso for informado apenas dois parâmetros dará erro.'''

# def somar(a, b, c):
#     s = a + b + c
#     print(f'A soma é {s}')
#
# somar(4, 6)

'''Para contornar isso, deve se criar parâmetros opcionais,
como no exemplo abaixo:'''

# def somar(a = 0, b = 0, c = 0):
#     s = a + b + c
#     print(f'A soma é {s}')
#
# somar(2, 5)

'''Qualquer parâmetro que seja omitido, será substituido por 0 zero'''

# ESCOPO DE VARIÁVEIS

'''Toda variável definida fora de uma função é tem o escopo global.
Ou seja, ela pode agir dentro de uma função.
Mas uma criada dentro de um função, só pode agir dentro dela, escopo local.
Caso seja criado uma variável dentro de uma função com o mesmo nome,
 de outra de fora, elas serão diferentes'''

# def teste(b):
#     a = 8
#     b += 5
#     c = 2
#     print(f'A dentro vale {a}')
#     print(f'B dentro vale {b}')
#     print(f'C dentro vale {c}')
#     print()
#
# a = 5
# teste(a)
# print(f'A fora vale {a}')

'''Caso queira trasformar a variável dentro da função como global,
usar o comando global.'''

# def teste(b):
#     global a
#     a = 8
#     b += 5
#     c = 2
#     print(f'A dentro vale {a}')
#     print(f'B dentro vale {b}')
#     print(f'C dentro vale {c}')
#     print()
#
# a = 5
# teste(a)
# print(f'A fora vale {a}')

'''Assim a variável antes definida, será apagada.'''

#  RETORNO DE VALORES

# def soma(* num):
#     s = sum(num)
#     return s
#
# r1 = soma(4, 6, 5)
# r2 = soma(1, 8)
# r3 = soma(8.2, 1.8, 4.5)
#
# print(f'A soma dos valores é: {r1}, {r2} e {r3}')

# Exercício 101 - voto()
'''Importação de modulos ou pacotes que só serão utilizados dentro
de uma função, é melhor importa-lo dentro da função, economiza memória.
Isso é escopo de importação, escopo local'''

# def voto(n=0):
#     from datetime import date as dt
#     idade = dt.today().year - n
#     if idade < 16:
#         return f'Idade: {idade}\nNão vota.'
#     elif 16 <= idade < 18 or idade >= 65:
#         return f'Idade: {idade}\nVoto opcional.'
#     else:
#         return f'Idade: {idade}\nVoto obrigatório.'
#
#
# ano = int(input(f'Em que ano você nasceu? '))
# res = voto(ano)
# lin()
# print(res)

# Exercício 102 - fatorial()


# def fatorial(num, show=False):
#     from time import sleep as sl
#     """
#     -> Calcular o fatorial de um número.
#     :param num: O número a ser calculado;
#     :param show: (opcional) Mostrar ou não a conta;
#     :return: O valor do Fatorial de um número n.
#     """
#     if show:
#         lin()
#     calc = 1
#     for n in range(num, 0, -1):
#         if show:
#             sl(0.3)
#             print(f' {n} ', end='')
#             if n > 1:
#                 sl(0.3)
#                 print('x', end='')
#             else:
#                 print(f' = {calc}')
#                 lin()
#         calc *= n
#     return calc
#
#
# z = fatorial(5, show=True)
#
# y = fatorial(7)
#
# fatorial(8)
#
# help(fatorial)

# Ecercício 103 - ficha() jogador
#
# def ficha(nome, gols):
#     lin()
#     if not nome or nome.isnumeric():
#         nome = '<desconhecido>'
#     if not gols or not gols.isnumeric():
#         gols = '0'
#     print(f'O jogador {nome}, fez {gols} gol(s) no campeonato.')
#     lin()
#
# ficha(input('Nome do jogador: ').strip(), input('Total de gols: ').strip())

# Exercício 104 -
#
# def leiaint(a='Digite um número: '):
#     numer = '0123456789'
#     num = 'nada'
#     lin()
#     while num not in numer:
#         num = str(input(a))
#         if num not in numer:
#             print('\033[31mErro! Digite um número inteiro.\033[m')
#         lin()
#     num = int(num)
#     return num
#
#
# n = leiaint('Digite um número: ')
# print(f'Você acabou de digitar o número {n}')


# Exercício 105 - notas()

# def notas(* num, situ=False):
#     """
#     -> Para analizar notas e situações de vários alunos.
#     :param num: Um ou mais notas dos alunos (aceeita várias)
#     :param situ: valor opcional, para adicionar também a situação
#     :return: Dicionário com as informações sobre a turna
#     """
#     res = {}
#     res['total'] = len(num)
#     res['maior'] = round((max(num)), 2)
#     res['menor'] = round((min(num)), 2)
#     res['media'] = round((sum(num) / res['total']), 3)
#     if situ:
#         if res['media'] < 5:
#             res['situacao'] = 'reprovado'
#         elif 5 <= res['media'] <= 6.9:
#             res['situacao'] = 'recuperação'
#         else:
#             res['situacao'] = 'aprovado'
#     return res
#
#
# resp = notas(7.531, 8.679, 9.216, 4.281, 7.984, situ=True)
# print(resp)
#
# help(notas)

# Exercício 106 - interactive help
# from time import sleep as sl
#
# def titulo(txt):
#     print('-' * len(txt))
#     print(f'\033[1;36m{txt:^}\033[m')
#     print('-' * len(txt))
#
#
# def lin():
#     print('--' * 24)
#
#
# opc = ''
# while True:
#     titulo(' SISTEMA DE AJUDA PyHelp ')
#     opc = str(input(' Função, Biblioteca, Operadores etc > '))
#     lin()
#     if opc == 'fim':
#         break
#     print(f' Acessando manual do comando {opc} [', end='')
#     for c in range(0, 10):
#         print('■', end='')
#         sl(0.2)
#     print('] 100%')
#     sl(0.3)
#     lin()
#     print('\033[1;7m')
#     help(opc)
#     print('\033[m')
# print('\033[1;37m Até logo. \033[m')
# lin()

# Aula 22 - modulos e pacotes
# import uteis
#
# num = int(input('Digite um valor: '))
# fat = uteis.fatorial(num)
# dob = uteis.dobro(num)
# tri = uteis.triplo(num)
# print(f'O fatorial de {num} é {fat}')
# print(f'O dobro de {num} é {dob}')
# print(f'O triplo de {num} é {tri}')

# Exercício 106 - modulo moeda
# import moeda as md
#
# p = float(input('Digite o preço: '))
# print(f'A metade de {p} é {md.metade(p)}')
# print(f'O dobro de {p} é {md.dobro(p)}')
# print(f'Aumentando 13,6% de {p} fica {md.aumentar(p, 13.6)}')
# print(f'Diminudindo 0,7% de {p} fica {md.diminuir(p, 7)}')

# Exercício 107 - incrementar o modulo moeda com a def moeda
# import moeda as md
#
# p = float(input('Digite o preço: '))
# print(f'A metade de {md.moeda(p)} é {md.moeda(md.metade(p))}')
# print(f'O dobro de {md.moeda(p)} é {md.moeda(md.dobro(p))}')
# print(f'Aumentando 13,6% de {md.moeda(p)} fica {md.moeda(md.aumentar(p, 13.6))}')
# print(f'Diminudindo 0,7% de {md.moeda(p)} fica {md.moeda(md.diminuir(p, 7))}')

# Exercício 108 - incrementando parâmetro True para formatar
# import moeda as md
#
# p = float(input('Digite o preço: '))
# print(f'A metade de {md.moeda(p)} é {md.metade(p, True)}')
# print(f'O dobro de {md.moeda(p)} é {md.dobro(p, True)}')
# print(f'Aumentando 13,6% de {md.moeda(p)} fica {md.aumentar(p, 13.6, True)}')
# print(f'Diminudindo 0,7% de {md.moeda(p)} fica {md.diminuir(p, 7, True)}')

# Exercício 109 - def resumo dentro do modulo
# import moeda as md
#
# p = float(input('Digite o preço: '))
# md.resumo(p, 17.8, 0.3)

# Exercício 110 - criação de pacote

# Exercício 111 - modulo dado def leia_num() (último exercício)
from utilidades.dado import leia_num as ln
from utilidades.moeda import resumo as rs

p = ln('Digite o preço em USD: ')
z = rs(p, 78.9, 10.07, 'USD')

# Aula
