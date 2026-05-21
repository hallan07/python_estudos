# importar um biblioteca inteira
# from ctypes import py_object
#
# import math

# print('Olá mundo')
# print('''Mussum Ipsum, cacilds vidis litro abertis.
# Cevadis im ampola pa arma uma pindureta.
# Manduma pindureta quium dia nois paga.
# Delegadis gente finis, bibendum egestas augue arcu ut est.
# Detraxit consequat et quo num tendi nada.''') # outra forma de colocar texto inteiro com quebras


# importar apenas um comando
# from math import sqrt
#
# #raiz = sqrt()
# num = float(input('Digite um número: '))
# print('A raiz quadrada de {} é {:.4f}'.format(num,(sqrt(num))))

# import math
# from math import sqrt, floor

# num = float(input('Digite um número: '))
# print ('O número inteiro é {}'.format(int(num)))
# raiz = sqrt(num)
# print ('a raiz de {:.2f} é {:.2f}'.format(num, floor(raiz)))
#
# import random
# num = random.randint(1,100)
#
# print(num)


# exercício 016
# import pygame

'''num2 = float(input('Insira um número: '))
print('A porção inteira de {} é {:.0f}.'.format(num2,math.trunc(num2)))

num3 = float(input('Insira um número: '))
print('O número inserido é {} e sua porção inteira é {}.'.format(num3, int(num3)))'''

# exercício 017
'''co = float(input('Qual comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adijacente? '))
#hi = (co ** 2 + ca ** 2) ** (1/2)
hi = math.hypot(co, ca)
print('O valor da hipotenusa é {:.3f}'.format(hi))'''

# exercício 018
'''ag = float(input('Qual é o angulo? '))
sen = math.sin(math.radians(ag))
cos = math.cos(math.radians(ag))
tan = math.tan(math.radians(ag))
print('O SENO do ângulo {:.2f} é {:.2f}.'.format(ag,sen))
print('O COSSENO do ângulo {:.2f} é {:.2f}.'.format(ag,cos))
print('A TANGENTE do ângulo {:.2f} é {:.2f}.'.format(ag,tan))'''

# exercício 019
# from random import choice
# n1 = str(input('Nome do aluno 01: '))
# n2 = str(input('Nome do aluno 02: '))
# n3 = str(input('Nome do aluno 03: '))
# n4 = str(input('Nome do aluno 04: '))
# lista = [n1,n2,n3,n4]
# sorteio = choice(lista)
# print('O aluno escolhido foi: {}.'.format(sorteio))

# exercício 020
'''from random import shuffle
n1 = str(input('Aluno 01: '))
n2 = str(input('Aluno 02: '))
n3 = str(input('Aluno 03: '))
n4 = str(input('Aluno 04: '))
lista = [n1,n2,n3,n4]
shuffle(lista)
print('A ordem é {}.'.format(lista))'''

# exercício 021
'''esse código não está finalizando
import pygame
pygame.mixer.init()
pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()'''

# esse funciona e finaliza
'''import playsound
playsound.playsound('D:/Python/audio.mp3',True)'''

# Aula 09 - tratamento de texto
# frase = 'Curso em vídeo de Python'
# print(frase[9:15])
# frase2 = 'Hoje da pra lua colher mais canalhas'
# print(frase2[::6]) # 1:2:3 no 1 é onde começa a fatiar, 2 fim, 3 pular
# print(frase2.find('lua')) # find é encontrar, retorna a posição
# print(len(frase)) # len é o comprimento
# print(frase.count('o')) # contar quantos 'o' há
# print(frase.count('e',0,13)) # contagem de 'e' entre o 0 e 13
# print('Curso'in frase) # boleana para saber se há 'Curso' na string frase
# frase.replace('Pyhton', 'Android') # subistituir o primeiro pelo segundo termo
# por padrão uma string não muda, então para mudar textos deve-se atribuir de novo ex:
# frase = frase.replace('Python', 'Android') # como nesse exemplo, ou tb atribuir para outra variavel
# print(frase)
# frase.upper() # tudo em caixa alta
# frase.lower() # tudo minusulo
# print(frase.upper().count('O')) # caixa alta em toda string, contar os 'O' e printar
# frase.capitalize() # somente a primeira letra da string maiuscula
# frase.title() # todos as palavras maiusculas
# frase.replace('Python', 'Python   ')
# frase.strip()  # remover espaços no início e fim
# frase.rstrip() # remover espaços da direita
# frase.lstrip() # remos espaços da esquerda
# print(frase.split()) # divide a string em palavras dentro de uma lista. Há outras formas *estudar
# print(frase[2])
# dividido = frase.split() # aqui foi atribuido a uma nova variavel a divisão de frase, e foi enumerado a lista d palavras
# print(dividido[4]) # no primeiro couchete ele mostra o número do item dentro da lista
# print(dividido[2][1]) # aqui mesma coisa e no segundo couchete ele mostra a letra do item
# print(''.join(frase)) # ao contrário do split ele junta os itens da lista

# exercício 022 - tratamento de textos
# nome = input('Digite seu nome')
# print('Seu nome em caixa alta: ',nome.upper())
# print('Seu nome minúsculo: ',nome.lower())
# divisao = nome.split() # foi dividido para remover os espaços
# juncao = ''.join(divisao) # foi juntado para poder contar, agora sem espaços
# conta = len(juncao) # len faz a contagem
# print('Seu nome tem {} letras'.format(conta))
# primeiro = divisao[0]
# conta2 = len(primeiro)
# print('O primeiro nome tem {} letras'.format(conta2))

# outra forma
# nome = str(input('Escreva seu nome: ')).strip() #strip tira os espaços antes e depois, somente de str
# print('Seu nome em caixa alta é : ',nome.upper())
# print('Seu nome em minúscuo é: ',nome.lower())
# print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) # find retorna a posição, no caso do espaço


# exercício 023
# forma de string, assim resolve mas só pode ser feito com input de 4 dígitos
# num = (input('Insira um número: ')) # o python já trasforma em string normalmente
# print('Unidade de milhar: {}'.format(num[0])) # retorna a posição 0 ou seja aprimeira e assim por diante
# print('Unidade de centena: {}'.format(num[1]))
# print('Unidade de dezena: {}'.format(num[2]))
# print('Unidade: {}'.format(num[3]))

# forma númerica
# num2 = int(input('Insira um número: '))
# u = num2 // 1 % 10 # divisão inteira para separar dos números após a virgula
# d = num2 // 10 % 10 # e depois % retorna o resto da divisão, sendo 10 último número antes da virgula
# c = num2 // 100 % 10
# m = num2 // 1000 % 10
# print('Unidade de milhar: {}'.format(m))
# print('Unidade de centena: {}'.format(c))
# print('Unidade de dezena: {}'.format(d))
# print('Unidade: {}'.format(u))

# exercício 024
# cidade = input('Qual cidade você nasceu? ')
# divisao = cidade.lower().split()
# primeiro = divisao[0]
# bol = 'santo' in primeiro
# santo = (bol and print('O primeiro nome da cidade é Santo'))
# and usa o segundo argumento se o primeiro for TRUE
# santo2 = (bol or print('Não há Santo no primeiro nome da cidade'))
# or usa o segundo argumento se o primeiro for FALSO

# outra forma
# cid = str(input('Digite o nome da cidade: '))
# print(cid[:5].lower() == 'santo')

# exercicio 025
# nome = input('Insira seu nome: ')
# low = nome.lower()
# bol = 'silva' in low
# cond1 = bol and print('Há Silva em seu nome')
# cond2 = bol or print('Não há Silva em seu nome')

# outra forma
# nome = str(input('Insira seu nome: '))
# print('Há Silva no seu nome? {}'.format('silva' in nome.lower()))

# exercicio 026
# fra = input('Digite uma frase: ')
# low = fra.lower()
# cont = low.count('a')
# prime = low.find('a')+1
# print('Sua frase tem {} letras A.'.format(cont))
# print('A posição da primeira letra A é {}.'.format(prime))
# a terceira parte não funcionou

# outra form de fazer
# frase = str(input('Digite uma frase: ')).lower().strip()
# print('Sua frase tem {} letras A'.format(frase.count('a')))
# print('A primeira letra A da sua frase é na {} posição.'.format(frase.find('a')+1))
# print('A última letra A parece na {} posição.'.format(frase.rfind('a')+1))

# exercício 27
# n = str(input('Qual seu nome? ')).strip()
# nome = (n.split())
# print('Prazer em te conhecer.')
# print('Seu primeiro nome é {}.'.format(nome[0]))
# print('Seu último nome é {}'.format(nome[len(nome)-1]))

# Aula 10 - condições
# nome = str(input('Escreva seu nome: ')).strip()
# n = nome.lower().split()
# if n[0] == 'hallan': # a condição if é se condição(verdadeira) então faça o argumanto abaixo
#     print('Que nome bonito.')
# else: # a condição else é se o if for falso, então faça o argumento abaixo
#     print('Que nome normal.')
# print('Olá {}, prazer em te conhecer.'.format(nome))
# a condição simplificada tb pode ser feita
# print('Que nome bonito.') if n[0] == 'hallan' else print('Que nome normal')

# outra aplicação
# nota1 = float(input('Digite a primeira nota: '))
# nota2 = float(input('Digite a segunda nota: '))
# med = (nota1 + nota2) / 2
# print ('Sua média foi {:.2f}'.format(med))
# print('Parabéns! Você mereceu.') if med >= 6.0 else print('Isso não é bom, estude mais.')

# exercicio 28
# a máquina escolhe um número de 0 à 5 e eu tenho que adivinhar
# from random import choice as ch
# lista = [0,1,2,3,4,5]
# escolha = int(ch(lista))
# print('Máquina diz:')
# print("- Eu escolhi um número de 0 à 5. Você consegue adivinhar qual foi? Há 16,66% de chance.")
# qnum = int(input("Escreva: "))
# print('Máquina diz:')
# if escolha == qnum:
#     print('Parabéns você acertou! Eu tinha escolhido o número {} :D'.format(escolha))
# else:
#     print('Você errou, eu escolhi {}. Tente de novo :/'.format(escolha))

# outra forma
# from random import randint
# from time import sleep
# computador = randint(0,5)
# print('\o/|o|\o//o/' *5)
# print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
# print('-+-' *20)
# jogador = int(input('Em que número eu pensei? '))
# print('processando...')
# sleep(2) # simular o tempo de processamento, 2 segundo
# if jogador == computador:
#     print('Parabéns! Você consiguiu me vencer.')
# else:
#     print('Você não acertou. Eu pensei no número {} e não no {}'.format(computador,jogador))

# exercício 29
# vel = float(input('Qual a velocidade do carro? '))
# custo = float(vel-80)*7
# #print(custo)
# if vel > 80.00:
#     print('Você ultrapassou o limite de velocidade. Será Multado em R${:.2f}'.format(custo))
# else:
#     print('Sua velocidade é permitida.')

# outra forma
# velocidade = float(input('Qual a velocidade atual do carro? '))
# if velocidade > 80: # condição simples, que pode ser feito usando somento if
#     print('Multado! Você excedeu o limite permitido que é 80Km/h')
#     multa = (velocidade-80) * 7
#     print('Você deve pagar uma multa de R${:.2f}!'.format(multa)) # toda sequencia utilizando 'tab' é executada com a condição
# print('Tenha um bom dia. Dirija com segurança.')

# exercício 30
# num = float(input('Insira um número inteiro: '))
# calc = num%2 # para diferenciar par e impar, quando um numero inteiro par é dividido por 2 sempre sobra 0 no resto da divisão
# print(calc)
# if calc == 0:
#     print('Esse número é par.')
# else:
#     print('Esse número é impar.')

# exercício 31
# dist = float(input('Insira a distância da viajem em km: '))
# ate = float(dist*0.5)
# alem = float(dist*0.45)
# if dist <= 200:
#     print('Sua viajem é inferior a 200km e custará R${:.2f}'.format(ate))
# else:
#     print('Sua viajem é superior a 200km e custará R${:.2f}'.format(alem))

# outra forma
# distancia = float(input('Qual a distância da sua viagem? '))
# print('Você está prestes a começar uma viagem de {:.0f}Km.'.format(distancia))
# if distancia <= 200:
#     preco = distancia * 0.50
# else:
#     preco = distancia * 0.45
# print('E o preço da sua passagem será de R${:.2f}'.format(preco))

# exercício 32
# ano = int(input('Qual ano é: '))
# bisex = ano%4
# if bisex == 0:
#     print('O ano de {} é um ano bissexto.'.format(ano))
# else:
#     print('O ano de {} não é um ano bissexto.'.format(ano))

# outra forma
'''se o ano for bissexto: antes do and a sentança é verdadeira, pois o ano precisa ser multiplo de 4.
 Se o ano for muliplo de 100, então  não é bissexto, ou seja o resto daria 0. Como a sentença antes do or
 é diferente de 0, ou seja, não multiplo de 100,  ele passa para o ultimo filtro. Que analisa de o numero é
 multiplo de 400, sobrando o resto como 0. O or aqui está fazendo a função de verdadeiro.'''
# from datetime import date
# print('Que ano você quer analisar?')
# ano = int(input('Coloque 0 para analizar o ano atual da minha máquina. '))
# if ano == 0:
#     ano = date.today().year
# if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#     print('O ano de {} é bissexto'.format(ano))
# else:
#     print('O ano de {} não é bissexto'.format(ano))


# exercício 33
# a = input('Primeiro valor: ')
# b = input('Segundo valor: ')
# c = input('Terceiro valor: ')
# num = [a,b,c] # essa forma é separando cada input
#
# #num = list(input('Insira três números: ').strip()) # sem virgula e sem espaço no meio
# num.sort(reverse=True) # o sort organiza a lista, se reverse for True entao fica do maior para menor
# print('O maior número é {} e o menor é {}.'.format(num[0],num[len(num)-1]))

# outra forma
# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceito valor: '))
# # testando menor
# if a < b and a < c:
#     menor = a
# if b < a and b < c:
#     menor = b
# if c < a and c < b:
#     menor = c
# # testando maior
# if a > b and a > c:
#     maior = a
# if b > a and b > c:
#     maior = b
# if c > a and c > b:
#     maior = c
# print('O menor valor é o {}'.format(menor))
# print('O maior valor é o {}'.format(maior))


# outra forma mais simples
# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
# # testar o menor
# menor = a
# if b < a and b < c:
#     menor = b
# if c < a and c < b:
#     menor = c
# # testar o maior
# maior = a
# if b > a and b > c:
#     maior = b
# if c > a and c > b:
#     maior = c
# print('O menor valor é o {}'.format(menor))
# print('E o maior valor é o {}'.format(maior))

# exercício 34
# sal = float(input('Qual o salário? '))
# if sal > 1250:
#     print('Seu novo salário será R${}'.format(sal+(sal*0.1)))
# else:
#     print('Seu novo salário será R${}'.format(sal+(sal*0.15)))

# outra forma
# sal = float(input('Qual o valor do salário atual? R$ '))
# if sal <= 1250:
#     novo = (sal * 0.15) + sal
# else:
#     novo = (sal * 0.1) + sal
# print('Para um salário atual de R${:.2f} agora passa a ganhar R${:.2f}'.format(sal,novo))


# exercício 35
# print('Regra da condição de existência de um triângulo.')
# ret1 = float(input('Insira o comprimento da reta 01: ').strip())
# ret2 = float(input('Insirao comprimento da reta 02: ').strip())
# ret3 = float(input('Insira o comprimento da reta 03: ').strip())
# list = list([ret1,ret2,ret3])
# list.sort(reverse=True)
# subt = list[1] - list[2]
# soma = list[1] + list[2]
# if list[0] > subt:
#     if list[0] < soma: # aqui foi criado uma condição dentro de outra condição
#         print('É possivel fazer um triângulo com o comprimento das três retas.')
#     else:
#         print('Não é possivel fazer um triângulo com o comprimento das três retas.')
# else:
#     print('Não é possivel fazer um triângulo com o comprimento das três retas.')

# outra forma
# a = float(input('Primeira reta: '))
# b = float(input('Segunda reta: '))
# c = float(input('Terceira reta: '))
# if a < b + c and b < a + c and c < a + b:
#     print('É possível formar um triangulo com os três retas.')
# else:
#     print('Não é possível formar um triangulo com as retas apresentadas.')

# Aula 11 - bônus cores
# Para gerar cores no terminal será utilizado o padrão ANSI, \033[0;0;0m sendo a primeira posição a formatação do texto
# ou seja o estilo, e para isso tem-se as melhores que funcionam são:
# 0 = normal(sem formatação), 1 = Bold, 4 = sublinado, 7 = invertido cores de fundo e da forte
# para a segunda posição tem-se as cores da fonte que vão de 30 até 37:
# 30 = branco, 31 = vermelho, 32 = verde, 33 = amarelo, 34 = azul, 35 = roxo, 36 = ciano, 37 = cinza
# e a ultima posição será as cores de fundo, background:
# 40 = branco, 41 = vermelho, 42 = verde, 43 = amarelo, 44 = azul, 45 = roxo, 36 = ciano, 37 = cinza
# nas cores, se usar 0 ou deixar vazio, o python preenche com a cor padrão do terminal, cinza.
# se alterar as ordens das três formatações, não vai importar, o pyhton lê normalmente.
# print('\033[1;33;44mTeste')
# print('\033[1;30;46mTeste\033[m') # utilizando o comando vazio no final, é cancelado a formatação.
# a = 'Azul'
# b = 'Roxo'
# print('Essa é um tipo de foamatação para a cor \033[1;34;40m{}\033[m e \033[1;35;40m{}\033[m!'.format(a,b))
# # há outra forma de fazer, sendo a primeira chave para inserir a cor, a ultima para tirar
# print('Esse é outra forma de formatar cores como {}{}{} e também {}{}{}!!'.format('\033[1;34;40m',a,'\033[m','\033[1;35;40m',b,'\033[m'))
# # outra forma, com dicionário.
# form = {'azul':'\033[36m','bold':'\033[1m','bgbranco':'\033[40m','fecha':'\033[m'}
# print('Agora pode-se representar a cor {}{}{}{} utilizando um dicionário'.format(form['azul'],form['bgbranco'],a,form['fecha']))
# # utilizando dicionário assim fica mais complexo e trabalhoso, o correto é especificar as formatações
# # para utilizar cores de fontes, backgrounds e estilos tudo junto.

# Meu programa de formatação de texto
print('Programa de formatação de cores')
texto = str(input('Digite o texto: ')) # variável do texto digitado
print('Qual cor da fonte você deseja?')
print('1 - \033[1;30mBranco\033[m')
print('2 - \033[1;31mVermelho\033[m')
print('3 - \033[1;32mVerde\033[m')
print('4 - \033[1;33mAmarelo\033[m')
print('5 - \033[1;34mAzul\033[m')
print('6 - \033[1;35mRoxo\033[m')
print('7 - \033[1;36mCiano\033[m')
print('8 - \033[1;37mCinza\033[m')
font = int(input('Digite o número da cor para a fonte: ')) # variável referente a formatação do texto escolhido
print('Qual cor de background você deseja?')
print('1 - Branco   \033[40m          \033[m')
print('2 - Vermelho \033[41m          \033[m')
print('3 - Verde    \033[42m          \033[m')
print('4 - Amarelo  \033[43m          \033[m')
print('5 - Azul     \033[44m          \033[m')
print('6 - Roxo     \033[45m          \033[m')
print('7 - Ciano    \033[46m          \033[m')
print('8 - Cinza    \033[47m          \033[m')
bg = int(input('Escolha o número da cor de background: ')) # variável referente ao bg escolhido

# formatação do texto
if font == 1:
    fim = str('{}{}{}'.format('\033[1;30m',texto,'\033[m'))
if font == 2:
    fim = str('{}{}{}'.format('\033[1;31m',texto,'\033[m'))
if font == 3:
    fim = str('{}{}{}'.format('\033[1;32m',texto,'\033[m'))
if font == 4:
    fim = str('{}{}{}'.format('\033[1;33m',texto,'\033[m'))
if font == 5:
    fim = str('{}{}{}'.format('\033[1;34m',texto,'\033[m'))
if font == 6:
    fim = str('{}{}{}'.format('\033[1;35m',texto,'\033[m'))
if font == 7:
    fim = str('{}{}{}'.format('\033[1;36m',texto,'\033[m'))
if font == 8:
    fim = str('{}{}{}'.format('\033[1;37m',texto,'\033[m'))

# formatação do background
if bg == 1:
    fim = ('{}{}{}'.format('\033[40m',fim,'\033[m'))
if bg == 2:
    fim = ('{}{}{}'.format('\033[41m',fim,'\033[m'))
if bg == 3:
    fim = ('{}{}{}'.format('\033[42m',fim,'\033[m'))
if bg == 4:
    fim = ('{}{}{}'.format('\033[43m',fim,'\033[m'))
if bg == 5:
    fim = ('{}{}{}'.format('\033[44m',fim,'\033[m'))
if bg == 6:
    fim = ('{}{}{}'.format('\033[45m',fim,'\033[m'))
if bg == 7:
    fim = ('{}{}{}'.format('\033[46m',fim,'\033[m'))
if bg == 8:
    fim = ('{}{}{}'.format('\033[47m',fim,'\033[m'))

# mostrar formatação escolhida
print('Abaixo a formatação escolhida: ')
print(fim)
