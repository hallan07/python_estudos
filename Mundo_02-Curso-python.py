# Estrutura para tratamento de texto
# remoção de caracteres especiais
# pontos = '''!()-[]{};:'"“”\,<>./?@#$%^&*_~ªº¹²³'''
# frase = str('Q u al! quer? // <fra~^S>Ê')
# frase1 = ''
# for i in frase.lower():
#     if i not in pontos:
#       frase1 += i
# print(frase1)
# # Remoção de pontuações
# var0 = str(input('Tratamento de texto\nInsira uma frase: '))
# dic = {'á':'a','à':'a','ã':'a','â':'a','ä':'a','é':'e','è':'e','ê':'e','ë':'e','í':'i','ì':'i','î':'i','ï':'i','ó':'o','ò':'o','õ':'o','ô':'o','ö':'o','ú':'u','ù':'u','û':'u','ü':'u','ñ':'n','ç':'c'}
# var1 = ''
# for c in var0:
#     if c not in dic:
#         var1 += c
#     elif c in dic:
#         var1 += dic[c]
# print(var1)


# exercício 36
# print('Programa de financiamento imobiliário')
# casa = float(input('Insira valor da casa que você pretende financiar: R$ '))
# ano = int(input('Insira a quantidade de anos que você pretende pagar: '))
# sal = float(input('Insira seu salário atual: R$ '))
# if sal*0.3 >= casa/(ano*12):
#     print('Seu financiamento foi  aprovado!','\n'
#           'A mensalidade será de R${:.2f} em {} meses.'.format(casa/(ano*12),(12*ano)))
# else:
#     print('Desculpe, seu financiamento não pode ser provado.')

# exercício 37
# print('{}Programa de conversão de bases.{}'.format('\033[1;34m','\033[m'))
# val = int(input('Insira qualquer número sem vírgula: '))
# print('Escolha o número da respectiva base que você deseja converter?','\n',
#              '1 - Para converter em base binária','\n',
#              '2 - Para converter em base octal','\n',
#              '3 - Para converter em base hexadecimal')
# base = input()
# # correção se o número for 0 ou acima de 3
# if base == '0':
#     print('Por favor escolha um número entre 1 e 3 referente as conversões das bases.')
#     base = input()
# elif base > '3':
#     print('Por favor escolha um número entre 1 e 3 referente as conversões das bases.')
#     base = input()
# # condição para conversão de base
# if base == '1':
#     conver = bin(val) # bin é o comando para converter em base 2
#     nome = 'binária'
# elif base == '2':
#     conver = oct(val) # oct para base 8 ou octal
#     nome = 'octal'
# elif base == '3':
#     conver = hex(val) # hex para base 16 ou hexadecimal
#     nome = 'hexadecimal'
# # condição para classificar o nome do tipo de conversão
# print('{}O número {} convertido para base {} fica {}.{}'.format('\033[1;34m',val,nome,conver[2:],'\033[m'))

# outra forma
# num = int(input('Insira um número inteiro: '))
# print('''Escolha uma das bases para conversão:
# 1 - converter em base binária
# 2 - converter em base octal
# 3 - converter em base hexadecimal''')
# opcao = int(input('Escolha sua opção: '))
# for c in range(0,999):
#     if opcao <= 0 or opcao >= 4:
#         print('Por favor escolha uma opção entre 1 e 3.')
#         opcao = int(input('Escolha sua opção: '))
# if opcao == 1:
#     print('{}O número {} convertido em base binária é {}'.format('\033[1;36m',num,bin(num)[2:]))
# elif opcao == 2:
#     print('{}O número {} convertido em base octal é {}'.format('\033[1;36m',num,oct(num)[2:]))
# else:
#     print('{}O número {} convertido em base hexadecimal é {}.'.format('\033[1;36m',num,hex(num)[2:]))

# conversão binário inteiro e vice verso
# binario = bin(150)
# print(binario)
# inteiro = int(0b10010110)
# print(inteiro)

# exercício 38
# val1 = float(input('Primeiro valor: '))
# val2 = float(input('Segundo valor: '))
# if val1 > val2:
#     print('O primeiro valor, {}, é maior do que o segundo valor {}'.format(val1,val2))
# elif val2 > val1:
#     print('O segundo valor, {}, é maior do que o primeiro valor {}'.format(val2,val1))
# elif val1 == val2:
#     print('O primeiro e o segundo valor são iguais {}'.format(val1))

# exercicio 39
# from datetime import date
# print('{} Programa do tempo de alistamento no serviço militar {}'.format('\033[1;32;40m','\033[m'))
# ano = (date.today().year)
# nasci = int(input('Insira seu ano de nascimento: '))
# idade = ano - nasci
# if idade < 18:
#     falta = 18 - idade
#     saldo = ano + falta
#     print('Quem nasceu em {} tem {} anos em {}.'.format(nasci,idade,ano))
#     print('Falta {} anos para você se alistar. Deverá comparecer no ano de {}'.format(falta,saldo))
# elif idade == 18:
#     print('Quem nasceu em {} tem {} anos em {}.'.format(nasci, idade, ano))
#     print('Está na hora de se alistar.')
# elif idade > 18:
#     falta = idade - 18
#     saldo = ano - falta
#     print('Quem nasceu em {} tem {} anos em {}.'.format(nasci, idade, ano))
#     print('Já passou {} anos que você deveria ter se alistado!'.format(falta))
#     print('Você deveria ter se alistado no ano de {}.'.format(saldo))

# exercicio 40
# nota1 = float(input('Insira a primeira nota: '))
# nota2 = float(input('Insira a segunda nota: '))
# med = (nota1 + nota2) / 2
# if med >= 7:
#     print('{}Parabéns você foi aprovado!'.format('\033[1;34m'),'\n',
#           'Sua média final é {:.2f}{}'.format(med,'\033[m'))
# elif med < 5:
#     print('{}Você foi reprovado!'.format('\033[1;31m'),'\n',
#           'Sua média final é {:.2f}{}'.format(med,'\033[m'))
# #elif med > 5 and med < 7:
# elif 5 <= med <= 6.99:
#     print('{}Você ficou de recuperação.'.format('\033[1;33m'),'\n',
#          'Sua média final é {:.2f}{}'.format(med,'\033[m'))

# exercicio 41
# from datetime import date
# cor = '\033[1;30;46m'
# fecha = '\033[m'
# print('{} Programa da confederação nacional de natação {}'.format('\033[1;36;40m',fecha))
# nasc = int(input('Insira o ano de nascimento do atleta: '))
# ano = (date.today().year)
# idade = ano - nasc
# print('{} O atleta tem {} anos. {}'.format(cor,idade,fecha))
# if idade <= 9:
#     print('{} Classificação: Atleta Mirim {}'.format(cor,fecha))
# elif idade <= 14:
#     print('{} Classificação: Atleta Infantil. {}'.format(cor,fecha))
# elif idade <= 19:
#     print('{} Classificação: Atleta Junior {}'.format(cor,fecha))
# elif idade <= 25:
#     print('{} Classificação: Atleta Sênior {}'.format(cor,fecha))
# else:
#     print('{} Classificação: Atleta Master {}'.format(cor,fecha))

# exercicio 42
# condição de exitência de triângulo:
# um de seus lados deve ser maior que o valor da diferença dos outros dois lados
# e menor que a soma dos outros dois lados
# print('{} Programa de definição de um triângulo {}'.format('\033[1;35;40m','\033[m'))
# r1 = float(input('Insira o comprimento da primeira reta: '))
# r2 = float(input('Insira o comprimento da segunda reta: '))
# r3 = float(input('Insira o comprimento da terceira reta: '))
# # condição que define o maior
# maior = r1
# if r3 < r2 > r1:
#     maior = r2
# elif r2 < r3 > r1:
#     maior = r3
# # condição que define o comprimento do meio
# meio = r1
# if r1 > r2 > r3:
#     meio = r2
# elif r1 > r3 > r2:
#     meio = r3
# # condição que define a menor
# menor = r1
# if r3 > r2 < r1:
#     menor = r2
# elif r2 > r3 < r1:
#     menor = r3
# # definição de tipo do triângulo
# # equilátero
# if r1 == r2 == r3:
#     tipo = 'equilátero'
# # escaleno
# elif r1 != r2 != r3 != r1:
#     tipo = 'escaleno'
# # isósceles
# else:
#     tipo = 'isósceles'
# # antiga
# '''if r3 != r1 == r2:
#     tipo = 'isósceles'
# elif r2 != r1 == r3:
#     tipo = 'isósceles'
# elif r1 != r3 == r2:
#     tipo = 'isósceles' '''
# # saber se o maior é menor que a soma e maior que a diferença dos outros lados
# if (meio + menor) > maior > (meio - menor):
#     print('{} É possível existir um triângulo {} com as medidas apresentadas. {}'.format('\033[1;36m',tipo,'\033[m'))
# else:
#     print('{} Não é possível existir um triângulo com as medidas apresetadas. {}'.format('\033[1;31m','\033[m'))

'''r1 = float(input('Reta 01: '))
r2 = float(input('Reta 02: '))
r3 = float(input('Reta 03: '))
lis = list([r1,r2,r3])'''
# lis = list([float(input('Reta 01: ')),float(input('Reta 02: ')),float(input('Reta 03: '))])
# lis.sort() # max é lis[2], med é lis[1], min é lis[0]
# print(lis[2],lis[1],lis[0])
# if lis[2] == lis[1] == lis[0]:
#     print('{}É possível formar um triângulo equilátero (três lados iguais).'.format('\033[1;36m'))
# elif (lis[1] - lis[0]) < lis[2] < (lis[1] + lis[0]) and lis[2] != lis[1] != lis[0] != lis[2]:
#     print('{}É possível formar um triângulo escaleno (todos lados diferentes).'.format('\033[1;36m'))
# elif (lis[1] - lis[0]) < lis[2] < (lis[1] + lis[0]) and lis[2] == lis[1] or lis[1] == lis[0] or lis[0] == lis[2]:
#     print('{}É possível formar um triângulo isósceles (dois lados iguais).'.format('\033[1;36m'))
# else:
#     print('{}Não é possivel formar um triângulo'.format('\033[1;31m'))

# exercicio 43
# print('{} Programa de cálculo do IMC (índice de massa corporal). {}'.format('\033[1;30;44m','\033[m'))
# altura = float(input('Insira sua altura em metros: '))
# peso = float(input('Insira seu peso em kg: '))
# imc = peso / (altura ** 2)
# print('{}Seu IMC é {:.2f}{}'.format('\033[1;37m',imc,'\033[m'))
# # classificação do IMC
# if 0 <= imc <= 16.9:
#     print('{}Você está muito abaixo do peso.{}'.format('\033[1;31m', '\033[m'))
#     print('{}E pode ter queda de cabelo, infertilidade, ausência menstrual.{}'.format('\033[1;31m', '\033[m'))
# elif 17 <= imc <= 18.4:
#     print('{}Você está abaixo do seu peso.{}'.format('\033[1;31m', '\033[m'))
#     print('{}E pode ter fadiga, stress e ansiedade.{}'.format('\033[1;31m', '\033[m'))
# elif 18.5 <= imc <= 24.9:
#     print('{}Parabéns, seu peso está normal.{}'.format('\033[1;36m', '\033[m'))
#     print('{}Você tem menor risco de doenças cardíacas e vasculares.{}'.format('\033[1;36m', '\033[m'))
# elif 25 <= imc <=29.9:
#     print('{}Você está acima do seu peso.{}'.format('\033[1;31m', '\033[m'))
#     print('{}E pode ter fadiga, má circulação e varizes.{}'.format('\033[1;31m', '\033[m'))
# elif 30 <= imc <= 34.9:
#     print('{}Você está acima do seu peso, obesidade de 1ª grau.{}'.format('\033[1;31m', '\033[m'))
#     print('{}E pode desenvolver diabetes, angina, infarto, aterosclerose.{}'.format('\033[1;31m', '\033[m'))
# elif 35 <= imc <= 40:
#     print('{}Você está acima do seu peso, obesidade de 2ª grau.{}'.format('\033[1;31m', '\033[m'))
#     print('{}E pode desenvolver apneia do sono, falta de ar.{}'.format('\033[1;31m', '\033[m'))
# else:
#     print('{}Você está acima do seu peso, obesidade de maior grau existente. Cuidado!{}'.format('\033[1;31m', '\033[m'))
#     print('{}E pode desenvolver refluxo, dificuldade para se mover, escaras, diabetes, infarto, AVC.{}'.format('\033[1;31m', '\033[m'))

# exericio 44
# {:=^47} o = é um texto, o ^ é centralizado e 47 é a quantidade de espaços total junto com texto
# print('{} {:=^47} {}'.format('\033[1;37;40m',' Cálculo da forma de pagamento ','\033[m'))
# preco = float(input('Insira o preço do produto R$ '))
# print('Qual forma de pagamento?\n'
#       '1 - Para à vista no dinheiro ou cheque.(10% desconto);\n'
#       '2 - Para à vista no cartão.(5% desconto);\n'
#       '3 - Para parcelado em até 2x no cartão.(preço normal);\n'
#       '4 - Para parcelado em 3x ou mais no cartão.(20% de juros)')
# condi = int(input('Selecione uma opção: '))
# # seleção da condição de pagamento
# if condi == 1:
#     final = preco - (preco * 0.1)
#     forma = ' com desconto de 10%. '
# elif condi == 2:
#     final = preco - (preco * 0.05)
#     forma = ' com desconto de 5%. '
# elif condi == 3:
#     final = preco
#     forma = ' em 2x de {:.2f} sem juros. '.format(final/2)
# elif condi == 4:
#     final = preco + (preco * 0.2)
#     par = int(input('Digite o número de parcela: '))
#     forma = ' em {}x de {:.2f}, já com o juros de 20%. '.format(par,final/par)
# print('{} O preço total do produto será R${:.2f}{}{}'.format('\033[1;37;40m',final,forma,'\033[m'))

# exercicio 45
# from random import randint
# #import emoji
# print('{} Jokempô {}'.format('\033[1;30;46m','\033[m'))
# print('{}-={}'.format('\033[1;36m','\033[m')*20)
# print('Qual você quer jogar?\n'
#       '1 - Pedra\n'
#       '2 - Papel\n'
#       '3 - Tesoura')
# escolha = int(input('Insira o número: '))
# maquina = randint(1,3)
# if escolha <= 0 or escolha >= 4:
#     escolha = int(input('Por favor escolha um número entre 1 e 3: '))
# print('{}-={}'.format('\033[1;36m','\033[m')*20)
# if escolha == 1 and maquina == 3:
#     print('{}Parabéns você ganhou! A máquina escolheu Tesoura.{}'.format('\033[1;36m','\033[m'))
# elif escolha == 1 and maquina == 2:
#     print('{}Você perdeu! A máquina escolheu Papel.{}'.format('\033[1;31m','\033[m'))
# elif escolha == 1 and maquina == 1:
#     print('Ninguém ganhou, ambos escolheram Pedra.')
# elif escolha == 2 and maquina == 1:
#     print('{}Parabéns você ganhou! A máquina escolheu Pedra.{}'.format('\033[1;36m','\033[m'))
# elif escolha == 2 and maquina == 3:
#     print('{}Você perdeu! A máquina escolheu Tesoura.{}'.format('\033[1;31m','\033[m'))
# elif escolha == 2 and maquina == 2:
#     print('Ninguém ganhou, ambos escolheram Papel.')
# elif escolha == 3 and maquina == 2:
#     print('{}Parabéns você ganhou! A máquina escolheu Papel.{}'.format('\033[1;36m','\033[m'))
# elif escolha == 3 and maquina == 1:
#     print('{}Você perdeu! A máquina escolheu Pedra.{}'.format('\033[1;31m','\033[m'))
# elif escolha == 3 and maquina == 3:
#     print('Ninguém ganhou, ambos escolheram Tesoura.')

# print(emoji.emojize('Python is :fist:'))

# outra forma
# from random import randint as ran
# from time import sleep as sl
# itens = ('','Pedra', 'Papel', 'Tesoura')
# pc = ran(1,3)
# print('''Escolha de 1 a 3:
# 1 - Pedra
# 2 - Papel
# 3 - Tesoura''')
# escolha = int(input('Digite: '))
# if escolha <= 0 or escolha >= 4:
#     escolha = int(input('Por favor escolha um número de 1 à 3: '))
# print('{}--'.format('\033[1;37m')*26)
# print('{}JO'.format('\033[1;37m')), sl(0.6)
# print('{}KEM'.format('\033[1;37m')), sl(0.6)
# print('{}PÔ!'.format('\033[1;37m'))
# print('A maquina escolheu {} e você escolheu {}.{}'.format(itens[pc], itens[escolha], '\033[m'))
# print('{}-='.format('\033[1;37m')*26)
# if escolha == pc:
#     print('{} {: ^49} {}'.format('\033[1;7m',' Ninguém ganhou. ','\033[m'))
# if escolha == 1:
#     if pc == 2:
#         print('{}{: ^49}{}'.format('\033[1;31;40m','Você perdeu.','\033[m'))
#     elif pc == 3:
#         print('{}{: ^49}{}'.format('\033[1;36;40m','Você venceu!','\033[m'))
# elif escolha == 2:
#     if pc == 1:
#         print('{}{: ^49}{}'.format('\033[1;36;40m','Você venceu!','\033[m'))
#     elif pc == 3:
#         print('{}{: ^49}{}'.format('\033[1;31;40m','Você perdeu.','\033[m'))
# elif escolha == 3:
#     if pc == 1:
#         print('{}{: ^49}{}'.format('\033[1;31;40m','Você perdeu.','\033[m'))
#     elif pc == 2:
#         print('{}{: ^49}{}'.format('\033[1;36;40m','Você venceu!','\033[m'))
# print('{}-='.format('\033[1;37m')*26)

# Aula 13
# contagem regressiva para os fogos de artifícios
# na ultima posição o python para, ou sej, ele não conta a ultima
# i = int(input('Inicio: ')) # é de onde começa a contar para repetição
# f = int(input('Final: ')) # é o final da contagem das repetições
# p = int(input('Passo: ')) # é a cadência da repetição, se for 2 é de 2 em 2, se for -1 é de 1 em 1 diminuindo
# for c in range(i,f,p):
#     print(c)

# estrutura que possibilita somar os valores
# s = 0
# for c in range(0,4):
#     n = int(input('Digite um valor: '))
#     s = s + n # também pode ser escrito como s += n
# print('A soma dos valores é {}'.format(s))

# exemplo de repetição de lista
# lista = ('acabaxi', 'banana', 'morango', 'maçã', 'pêra')
# for c in range(0,5):
#     print(c,lista[c])

# exercicio 46
# from time import sleep as sl
# print('{}Conatem regressiva para estourar os fogos:{}'.format('\033[1;7;30m','\033[m'))
# for c in range(10, -1, -1):
#     print(c)
#     sl(1)
# print('''{}KABOOOMMMM!!!{}
# ...estouram os fogos de artifícios.'''.format('\033[1;31m','\033[m'))

# solução encontrada no comentário do video
# import emoji
# from time import sleep
# print("="*14,"\033[037mDesafio 44, Version 1.0\033[0;0m - \033[37mPYTHON\033[0;0m","="*14)
# print("="*20,"\033[31mContagem de FOGOS!!!\033[0;0m","="*20,"\nAperte ENTER para iniciar a \033[32mCONTAGEM...\033[0;0m")
# ok = input("")
# print("VAI COMEÇAR EM....")
# for c in range (10,-1,-1):
#     sleep(1)
#     print("\033[32m{}\033[0;0m".format(c))
# print("="*6,"\033[32mAEOOOOOOOOOOOOOOO FOOOOGOOOSSS POHHAAAAAA, MORRAM CACHORROS\033[0;0m","="*6)#DESCULPA
# print(emoji.emojize("""
# \033[034m
# \033[31mA\033[34m
# ⊂_ヽ\033[31mM\033[34m
# 　 ＼＼ \033[31mO\033[34m＿
# 　　 ＼(　•_•) \033[31mF\033[34m
# 　　　 <　⌒ヽ \033[31mO\033[34m
# 　　　/ 　 へ＼ \033[31mG\033[34m
# 　　 /　　/　＼＼ \033[31mO\033[34m
# 　　 ﾚ　ノ　　 ヽ_つ \033[31mS\033[34m
# 　　/　/ \033[31mD\033[34m
# 　 /　/| \033[31mE\033[34m
# 　(　(ヽ
# 　|　|、＼ \033[32mARTIFÍCIOS\033[34m  :fireworks: :fireworks: :fireworks: :fireworks: :fireworks:
# 　| 丿 ＼ ⌒)   :clap::clap: :fire::fire:
# 　| |　　) /
# `ノ )　 Lﾉ
# (_／/
# \033[0;0m
# """,use_aliases=True))
# print("\033[37mFim...")
# #=============================================================================

# exercicio 47 - numeros pares de 0 a 51
# for c in range(0,51,2):
#     print('.',end='')
#     print(c, end=' ') # o end é utilizado para a linha não termnar

# exercicio 48
# soma entre todos os números ípares que são multiplos de 3
# s = 0
# for c in range(3, 496, 2):
# #   if c % 2 == 1 and c % 3 == 0: # com passo de 2 em dois não é necessário contar números não ímpares
#     if c % 3 == 0:
#         print(c, end='. ')
#         s = (s + c)
# print('\nA soma dos números ímpares multiplos de 3 de 0 à 500 é {}'.format(s))

# exercicio 49 - Tabuada
# print('Programa de tabuada')
# num = float(input('Insira um número: '))
# print('A tabuada do {} é:'.format(num))
# for c in range(1,11):
#     print('{:.0f} X {:.0f} = {:.2f}'.format(num,c,c*num))

# exercicio 50 - soma dos pares
# s = 0
# cont = 0
# for c in range(1,7):
#     val = int(input('Insira um valor: '))
#     if val % 2 == 0:
#         s += val # soma de s = s + val é representada dessa forma
#         cont += 1
# print('Você informou {} números pares e a soma é {}'.format(cont,s))

# exercicio 51 - PA progressão aritimética
# 4, 7, 10, 13... etc a diferença entre os números é 3, uma costante que se chama Razão 'r'
# a1,a2,a3,a4... etc PA = progressão aritimética
# print('{}Progressão aritimética{}'.format('\033[1m','\033[m'))
# inicio = int(input('Insira o início da PA: '))
# razao = int(input('Insira a razão da PA: '))
# fim = int(inicio + (razao * 10))
# if razao == 0:
#     tipo = 'constante'
# elif razao > 0:
#     tipo = 'crescente'
# else:
#     tipo = 'decrescente'
# print('{}-=-'.format('\033[1m')*14)
# print('''Progressão Aritimética do tipo {}.
# Seus 10 primeiros termos são:'''.format(tipo))
# cont = 0
# if razao != 0:
#     for c in range(inicio,fim,razao):
#         cont += 1
#         print(c,end='')
#         if cont != 10:
#              print(' ➝ ', end='')
#     print('\n')
# elif razao == 0:
#     for c in range(0,10):
#         cont += 1
#         print(inicio, end='')
#         if cont != 10:
#             print(' ➝ ', end='')
#     print('\n')
# print('{}-=-{}'.format('\033[1m','\033[m')*14)

# segunda forma, mais simples
# pri = int(input('PROGRESSÃO ARITIMÉTICA\nInsira o primeiro termo: '))
# raz = int(input('Insira a Razão: '))
# fim = pri + (raz * 10)
# print('A PA é: ',end='')
# if raz == 0:
#     for c in range(0,10):
#       print(pri,end=' ')
# if raz != 0:
#     for c in range(pri,fim,raz):
#       print(c, end='')

# forma encontrada nos comentários, funciona de todas as formas
# num = int(input('\nDigite o Primeiro número da PA: '))
# razão = int(input('Digite a Razão da PA: '))
# for c in range(1, 11):
#     print(num, end=' ')
#     num += razão

# outra forma mais simples
# n1=int(input('PROGRESSÃO ARITIMÉTICA\nInsira o primeiro termo: '))
# n2=int(input('Insira a Razão: '))
# for c in range(0,10):
# 	print('{}'.format(n1+(n2*c)),end=' ')

# exercicio 52 - numero primo
# num = int(input('\033[1mPrograma de números primos.\033[m \nDigite um número: '))
# txt = 'é primo.'
# for c in range(1, num + 1):
# #    print(c,end=' ')
#     if num % c == 0 and num != c and c != 1 or num <= 1:
#         txt = ('não é primo.')
# print('\n')
# print('{} O número {} {} {}'.format('\033[1;7m', num, txt, '\033[m'))

# outra forma
# num = int(input('IDENTIFICAÇÃO DE NÚMERO PRIMO\nInsira um número: '))
# cont = 0
# for c in range(1, num + 1):
#     if num % c ==0:
#         cont += 1
#         print('\033[1;36m', end='')
#     else:
#         print('\033[1;31m', end='')
#     print(c,'\033[m',end='')
# if cont == 2:
#     print('\n{}O número {} é um Primo.{}'.format('\033[1;36m', num ,'\033[m'))
# else:
#     print('\n{}O número {} não é Primo.{}'.format('\033[1;31m', num, '\033[m'))


# exercício 53 - palíndromo identificação
# abaixo a frase é colocada minúscula e dividida as palvras em lista
# from unidecode import unidecode as un
# frase = input('{}Identificação de palíndromo{}\nDigite uma frase: '.format('\033[1m','\033[m')).lower().split()
# txt0 = un(''.join(frase)) # a frase foi juntada para remover os espaços e un de unidecode para remover acentuação
# # remover pontuação com repetição
# txt = ''
# pontuacoes = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
# for i in txt0:
#    if i not in pontuacoes:
#        txt = txt + i
#
# cont = int(len(txt))
# if cont % 2 == 1: # tratando de frases com número de caracteres ímpares
#     loop = int((cont -1) / 2)
# elif cont % 2 == 0:
#     loop = int((cont / 2))
# compa = 0
# pos1 = int(0)
# pos2 = int(cont-1)
# for c in range(0,loop):
#     if txt[pos1] == txt[pos2]:
#         compa = compa + 1
#     pos1 = pos1 + 1
#     pos2 = pos2 - 1
# if pos1 == compa:
#     print('{} O frase é palíndromo. {}'.format('\033[1;7;36m','\033[m'))
#     print('{} E possui {} letras repetidas das {} totais. {}'.format('\033[1;7;36m',compa,cont,'\033[m'))
# else:
#     print('{} O texto não é palíndromo. {}'.format('\033[1;7;31m','\033[m'))

# Solução encontrada na net
# frase = str(input('Insira uma frase ou palavra: ')).replace(' ', '').upper() # o replace dessa forma retira espaços
# if frase == frase[::-1]: # esse comando inverte a frase
#     print('É palíndromo')
# else:
#     print('Não é palíndromo')

# Nova forma
# frase0 = str(input('DETCÇÃO DE PALÍNDROMO\nInsira uma frase: ')).lower()
# frase1 = ''
# pontos = ''' !()-[]{};:'"“”\,<>./?@#$%^&*_~'''
# for c in frase0:
#     if c not in pontos:
#         frase1 += c
# print('Sem pontos: ',frase1,'Invertida: ',frase1[::-1])
# if frase1 == frase1[::-1]:
#     print('{}A frase é palíndromo.'.format('\033[1;36m'))
# else:
#     print('{}A frase não é palíndromo.'.format('\033[1;31m'))

# exercício 54 - maioridade 21
# from datetime import date
# ano = date.today().year
# maior = 0
# menor = 0
# for c in range(1,8):
#     nasc = int(input('Digite o ano de nascimento da pessoa {}: '.format(c)))
#     if ano - nasc < 0 or nasc < 0:
#         nasc = int(input('Por favor digite um ano válido para a pessoa {}: '.format(c)))
#     if ano - nasc >= 21:
#         maior = maior + 1
#     else:
#         menor = menor + 1
# print('{} Há {} pessoas maiores de idade e {} menores. {} (21 anos)'.format('\033[1;7m',maior,menor,'\033[m'))

# outra forma
# from datetime import date as dt
# ano = dt.today().year
# idamaior = 0
# idamenor = 0
# for c in range(1, 8):
#     nasc = int(input('Insira o ano de nescimento da {}ª pessoa: '.format(c)))
#     idade = ano - nasc
#     if idade >= 21:
#         idamaior += 1
#     else:
#         idamenor += 1
# print('Há {} pessoas maiores de idade.'.format(idamaior))
# print('E {} pessoas menores de idade.'.format(idamenor))

# exercício 55 - peso maior e menor
# for c in range(1,6):
#     peso = float(input('Insira o peso da pessoa {}: '.format(c)))
#     if c == 1:
#         pess1 = peso
#         pessoa1 = 'pessoa {}'.format(c)
#     elif c == 2:
#         pess2 = peso
#         pessoa2 = 'pessoa {}'.format(c)
#     elif c == 3:
#         pess3 = peso
#         pessoa3 = 'pessoa {}'.format(c)
#     elif c == 4:
#         pess4 = peso
#         pessoa4 = 'pessoa {}'.format(c)
#     elif c == 5:
#         pess5 = peso
#         pessoa5 = 'pessoa {}'.format(c)
# lista = [pess1,pess2,pess3,pess4,pess5]
# # definição do maior
# if pess2 < pess1 > pess3 and pess4 < pess1 > pess5:
#     maior = pessoa1
# elif pess1 < pess2 > pess3 and pess4 < pess2 > pess5:
#     maior = pessoa2
# elif pess1 < pess3 > pess2 and pess4 < pess3 > pess5:
#     maior = pessoa3
# elif pess1 < pess4 > pess2 and pess3 < pess4 > pess5:
#     maior = pessoa4
# elif pess1 < pess5 > pess2 and pess3 < pess5 > pess4:
#     maior = pessoa5
# # definição do menor
# if pess2 > pess1 < pess3 and pess4 > pess1 < pess5:
#     menor = pessoa1
# elif pess1 > pess2 < pess3 and pess4 > pess2 < pess5:
#     menor = pessoa2
# elif pess1 > pess3 < pess2 and pess4 > pess3 < pess5:
#     menor = pessoa3
# elif pess1 > pess4 < pess2 and pess3 > pess4 < pess5:
#     menor = pessoa4
# elif pess1 > pess5 < pess2 and pess3 > pess5 < pess4:
#     menor = pessoa5
# lista.sort()
# print('{}--'.format('\033[1m')*22)
# print('A pessoa mais pesada é a {} com {:.2f}Kg.'.format(maior,lista[4]))
# print('E a pessoa mais leve é a {} com {:.2f}Kg.'.format(menor,lista[0]))
# print('{}--'.format('\033[1m')*22)

# uma outra forma com complemento
# maior = 0
# menor = 0
# for c in range(1, 6):
#     peso = float(input('Peso da {}ª pessoa: '.format(c)))
#     if c == 1:
#         maior = peso
#         menor = peso
#         pess_maior = c
#         pess_menor = c
#     else:
#         if peso > maior:
#             maior = peso
#             pess_maior = c
#         elif peso < menor:
#             menor = peso
#             pess_menor = c
# print('A {}ª pessoa é a mais pesada, com {} Kg'.format(pess_maior, maior))
# print('E a {}ª pessoa é a mais leve, com {} Kg'.format(pess_menor, menor))

# formas encontradas nos comentários
# print('VERIFICANDO O MENOR E O MAIOR PESO\n')
#
# pesos = []  # Lista para armazenar os pesos digitados.
#
# for c in range(1, 4):  # Percorre o laço 5 vezes.
#     peso = float(input(f'Peso da {c}ª pessoa em Kg: '))  # Recebe pesos de 5 pessoas.
#     pesos.append(peso)  # Coloca na lista.
#
# # Mostra o menor e o maior peso da lista digitados.
# print(f'\nO menor peso lido foi {min(pesos):.1f}Kg.\n' #o .format foi adicionado com o f no inicio do print
#       f'O maior peso lido foi {max(pesos):.1f}Kg.') # e foi fomatada dentro do espaço onde vai a variável

# outra forma encontrada nos comentários e modificada
# pesos = [float(input(f'Informe o peso da pessoa {c+1}: ')) for c in range(3)]
# print(f'A pessoa mais pesada tem {max(pesos)} Kg\nE a mais leve {min(pesos)} Kg')

# a forma mais simples que fiz
# lista = []
# for c in range(1, 6):
#     peso = float(input(f'Insira o peso da {c}ª pessoa: '))
#     lista.append(peso)
# print('A pessoa mais pesada tem {:.2f} Kg e a mais leve {:.2f} Kg'.format(max(lista), min(lista)))


# exercício 56 - ler nomes e retornar especificações
# from datetime import date
# num = 0
# ano = int(date.today().year)
# for c in range(0,4):
#     num = num + 1
#     if num == 1:
#         nome1 = str(input('Qual nome da pessoa 1: '))
#         nasc = int(input('Qual o ano de nascimento: '))
#         idade1 = int(ano - nasc)
#         print('Selecione o sexo\n1 - masculino\n2 - feminino')
#         esc = input('Digite: ')
#         if '0' >= esc >= '3':
#             esc = input(int('Por favor escolha um número entre 1 e 2: '))
#         elif esc == '1':
#             sexo1 = 'masculino'
#         elif esc == '2':
#             sexo1 = 'feminino'
#     elif num == 2:
#         nome2 = str(input('Qual nome da pessoa 2: '))
#         nasc = int(input('Qual o ano de nascimento: '))
#         idade2 = int(ano - nasc)
#         print('Sexo\n1 - masculino\n2 - feminino')
#         esc = input('Digite: ')
#         if '0' >= esc >= '3':
#             esc = input(int('Por favor escolha um número entre 1 e 2: '))
#         elif esc == '1':
#             sexo2 = 'masculino'
#         elif esc == '2':
#             sexo2 = 'feminino'
#     elif num == 3:
#         nome3 = str(input('Qual nome da pessoa 3: '))
#         nasc = int(input('Qual o ano de nascimento: '))
#         idade3 = int(ano - nasc)
#         print('Sexo\n1 - masculino\n2 - feminino')
#         esc = input('Digite: ')
#         if '0' >= esc >= '3':
#             esc = input(int('Por favor escolha um número entre 1 e 2: '))
#         elif esc == '1':
#             sexo3 = 'masculino'
#         elif esc == '2':
#             sexo3 = 'feminino'
#     elif num == 4:
#         nome4 = str(input('Qual nome da pessoa 4: '))
#         nasc = int(input('Qual o ano de nascimento: '))
#         idade4 = int(ano - nasc)
#         print('Sexo\n1 - masculino\n2 - feminino')
#         esc = input('Digite: ')
#         if '0' >= esc >= '3':
#             esc = input(int('Por favor escolha um número entre 1 e 2: '))
#         elif esc == '1':
#             sexo4 = 'masculino'
#         elif esc == '2':
#             sexo4 = 'feminino'
# # Média de idades
# print('{}--{}'.format('\033[1;37m','\033[m')*23)
# med = (idade1 + idade2 + idade3 + idade4) / 4
# print('{}A média das idades do grupo é {:.0f} anos.{}'.format('\033[1m',med,'\033[m'))
# # Homem mais velho
# if idade2 < idade1 > idade3 and idade1 > idade4 and sexo1 == 'masculino':
#     velho = nome1
#     idade = idade1
# elif idade1 < idade2 > idade3 and idade2 > idade4 and sexo1 == 'masculino':
#     velho = nome2
#     idade = idade2
# elif idade1 < idade3 > idade2 and idade3 > idade4 and sexo1 == 'masculino':
#     velho = nome3
#     idade = idade3
# elif idade1 < idade4 > idade2 and idade4 > idade3 and sexo1 == 'masculino':
#     velho = nome4
#     idade = idade4
# print('{}O homem mais velho é o {}, ele tem {} anos.{}'.format('\033[1m',velho,idade,'\033[m'))
# # Mulher que tem menos de 20 anos
# idades = [idade1,idade2,idade3,idade4]
# sexos = [sexo1,sexo2,sexo3,sexo4]
# novinhas = 0
# for i in range(0,4):
#     if idades[i] < 20 and sexos[i] == 'feminino':
#         novinhas = novinhas + 1
# if novinhas == 1:
#     elas = 'mulher'
# elif novinhas > 1:
#     elas = 'mulheres'
# print('{}Há {} {} com menos de 20 anos.{}'.format('\033[1m',novinhas,elas,'\033[m'))
# print('{}--{}'.format('\033[1;37m','\033[m')*23)

# outra forma
# som = 0
# ida_velho = 0
# nome_velho = 'não há'
# novinha = 0
# elas = 'mulher'
# for c in range(1, 3):
#     nome = input(f'Nome da {c}ª pessoa: ').capitalize().strip()
#     idade = int(input(f'Idade de {nome}: '))
#     sexo = input('Sexo\nM - masculino\nF - feminino\nDigite: ').lower()
#     som += idade
#     if sexo == 'm' and idade > ida_velho:
#         ida_velho = idade
#         nome_velho = nome
#     elif sexo == 'f' and idade < 20:
#         novinha += 1
#     elif novinha > 1:
#         elas = 'mulheres'
# print(f'A média da idade do grupo é {som / 2}')
# print(f'O homem mais velho é o {nome_velho}, com a idade de {ida_velho} anos.')
# print(f'Há {novinha} {elas} com menos de 20 anos.')

# Aula 14
# loop infinito
# n = 1
# while n != 0: # condição para que o while pare (while = enquanto)
#     n += 1
#     print('n')

# exercicio 57 - enquanto sexo não for m ou f a repetição não para
# sexo = ''
# for c in range(1, 3):
#     nome = input(f'Nome da {c} pessoa: ').strip().capitalize()
#     idade = int(input(f'Qual a idade de {nome}: '))
#     while idade <= -1 or idade > 150:
#         idade = int(input('Por favor digite uma idade válida: '))
#     sexo = input(f'Qual sexo de {nome}\nM - masculino\nF - feminino\nDigite: ').lower()
#     while 'f' != sexo != 'm':
#         sexo = input('por favor digite M para masculino ou F para feminino: ').lower()

# exercicio 58 - jogo de adivinhação
# from random import randint
# print('--'*20)
# maq = randint(1, 10)
# vez = 1
# num = int(input('''ADIVINHE O NÚMERO
# Máquina diz: - Eu pensei em um número entre 1 e 10, tente adivinhar!
# Há 10% de chance: '''))
# print('--'*20)
# while num != maq:
#     if num > maq:
#         dica = 'um pouco menos.'
#     elif num < maq:
#         dica = 'um pouco mais'
#     num = int(input('Errou... {}\nTente de novo: '.format(dica)))
#     vez += 1
#     print('--' * 20)
# print(f'Máquina diz: Parabéns, você acertou! Eu pensei no número {maq}.\nFoi necessário {vez} tentativas para acertar.')
# print('--'*20)

# exercicio 59 - calculadora
# print('{:=^40}'.format(' Cálculadora '))
# opc = 0
# num1 = float(input('Número 01: '))
# num2 = float(input('Número 02: '))
# print('--'*20)
# while opc != 5:
#     opc = int(input('Escolha uma opção\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair\nSelecione: '))
#     if opc == 1:
#         print('--' * 20)
#         print('{} Soma: {:.2f}{}'.format('\033[1;7m', num1 + num2, '\033[m'))
#         print('--' * 20)
#     elif opc == 2:
#         print('--' * 20)
#         print('{}Multiplicação: {:.2f}{}'.format('\033[1;7m', num1 * num2, '\033[m'))
#         print('--' * 20)
#     elif opc == 3:
#         if num1 > num2:
#             max = num1
#         elif num2 > num1:
#             max = num2
#         print('--' * 20)
#         print('{}Maior: {:.2f}{}'.format('\033[1;7m', max, '\033[m'))
#         print('--' * 20)
#     elif opc == 4:
#         print('--' * 20)
#         num1 = float(input('Número 01: '))
#         num2 = float(input('Número 02: '))
#         print('--' * 20)
# print('{:=^40}'.format(' Programa Finalizado '))

# exercicio 60 - fatorial
# print('{:=^36}'.format(' FATORIAL '))
# num = int(input('Insira um número: '))
# print('--'*17)
# mult = num -2
# calc = int(num * (num -1))
# calc2 = calc
# print(f'\033[1;7m {num}! = {num} x {num -1} x ', end='')
# while mult != 1:
#     calc2 = mult * calc2
#     print(f'{mult} x ', end='')
#     mult += -1
# print('{} = {} {}'.format(mult, calc2, '\033[m'))
# print('--'*17)

# outra forma com modulo
# from math import factorial
# num = int(input('Insira um número: '))
# print(f'O fatorial de {num} é {factorial(num)}')

# outra forma tradicional
# num = int(input('Digite um número: '))
# c = num
# f = 1
# while c > 0:
#     print(f'{c}', end=' ')
#     print('x ' if c > 1 else '= ', end='')
#     f *= c # é a mesma coisa q isso f = f * c
#     c -= 1
# print(f'{f}')

# exercicio 61 - PA progressão aritimética com while
# print('{:=^36}'.format(' Progressão Aritimérica '))
# num = int(input('Insira um número: '))
# raz = int(input('Insira a razão: '))
# calc = 0
# cont = 10
# print('--'*17)
# print(f'\033[1;7m A PA de {num} é: {num} 🠖 ', end ='')
# while cont != 1:
#     cont += -1
#     calc = num + raz
#     num = calc
#     print(calc, end=' ')
#     if cont != 1:
#         print('🠖', end=' ')
# print('\033[m')

# outra forma
# pri = int(input('Insira um numero: '))
# num = pri
# raz = int(input('Insira a razão: '))
# cont = 0
# while cont != 10:
#     print(num, end='')
#     cont += 1
#     if cont < 10: print(' 🠖 ', end='')
#     num += raz

# exercicio 62 - PA melhorada
# print('{:=^46}'.format(' Progressão Aritimérica '))
# num = int(input('Insira um número: '))
# raz = int(input('Insira a razão: '))
# calc = 0
# cont = 10
# print('--'*23)
# print(num, end=' 🠖 ')
# while (cont -1) != 0:
#     while cont != 1:
#         cont += -1
#         calc = num + raz
#         num = calc
#         print(calc, '🠖 ', end=' ')
#     print('fim')
#     print('--' * 23)
#     cont = int(input('Deseja ver mais termos?\nDigite a quantidade: ')) +1
# print('Programa finalizado')

# outra forma
# pri = int(input('Insira um numero: '))
# num = pri
# raz = int(input('Insira a razão: '))
# cont = 0
# c = 10
# while c != 0:
#     while c != 0:
#         print(num, end='')
#         cont += 1
#         if c > 1: print(' 🠖 ', end='')
#         num += raz
#         c -= 1
#     c = int(input('\n[0] - Digite zero para parar\nDigite a quantidade de termos que pretende ver: '))
# print(f'Quantidade de PA feitas: {cont}\nPrograma finalizado')

#exercicio 63 - sequencia de Fibonacci - incompleto
# calc = 1
# calc2 = 1
# calc3 = 0
# print('Sequencia de Fibonacci')
# cont = int(input('Insira o número de termos: '))
# while (cont + 1) != 1:
#     if cont == 1:
#         print(f'\033[1;7m Fibonacci: {calc3} \033[m')
#     elif  cont == 2:
#         print(f'\033[1;7m Fibonacci: {calc3} 🠖 {calc} \033[m')
#     elif cont == 3:
#         print(f'\033[1;7m Fibonacci: {calc3} 🠖 {calc} 🠖 {calc2} \033[m')
#     elif cont >= 4:
#         cont = (cont / 2)
#         print('cont: ', cont)
#         print(f'\033[1;7m Fibonacci: {calc3} 🠖 {calc} 🠖 {calc2}',end='')
#         while cont != 0:
#             calc3 = calc + calc2
#             print(f' 🠖 {calc3}', end='')
#             calc2 = calc3 + calc2
#             print(f' 🠖 {calc2}', end='')
#             calc = calc3
#             cont += -1
#     elif cont == 5:
#         cont = (cont // 2)
#         print('cont: ', cont)
#         print(f'\033[1;7m Fibonacci: {calc3} 🠖 {calc} 🠖 {calc2}', end='')
#         while cont != 0:
#             calc3 = calc + calc2
#             print(f' 🠖 {calc3}', end='')
#             calc2 = calc3 + calc2
#             print(f' 🠖 {calc2}', end='')
#             calc = calc3
#             cont += -1
#     cont = int(input(' \033[m\n[0] - Para finalizar\nInsira a quantidade de termos: '))
#     calc = 1
#     calc2 = 1
#     calc3 = 0
# print('\nPrograma finalizado')

# outra tentativa - incompleto
# cont = int(input('Loops: '))
# a = 1
# b = 0
# if cont == 1:
#     print(0)
# elif cont == 2:
#     print(0, 1)
# elif cont >= 3:
#     if cont % 2 == 1: # ímpar
#         cont = cont // 2
#         print(0, end=' ')
#         while cont != 0:
#             a = a + b
#             print(a, end=' ')
#             b = a + b
#             print(b, end=' ')
#             cont += -1
#     elif cont % 2 == 0: # par
#         print('a: ', a, 'b: ', b)
#         cont = cont / 2
#         while cont != 0:
#             a = a + b
#             print(a, end=' ')
#             b = a + b
#             print(b, end=' ')
#             cont += -1

# exercicio 63 - sequencia de Fibonacci - final
# print('{:=^50}'.format(' Sequência de Fibonacci '))
# num = 1
# cont = int(input('Insira o número de termos: '))
# while cont != 0:
#     if cont == 1:
#         print('--'*25)
#         print('Phi Φ: 0')
#         print('--' * 25)
#     elif cont == 2:
#         print('--' * 25)
#         print('Phi Φ: 0 🠖 1')
#         print('--' * 25)
#     elif cont == 3:
#         print('--' * 25)
#         print('Phi Φ: 0 🠖 1 🠖 1')
#         print('--' * 25)
#     elif cont >= 4:
#         cont = (cont -3)
#         print('--' * 25)
#         print('Phi Φ: 0 🠖 1 🠖 1 ', end='')
#         while cont != 0:
#             calc = 1.618 * num
#             calc = round(calc)
#             num = calc
#             print('🠖', num, end=' ')
#             cont += -1
#         print('\n')
#         print('--' * 25)
#         num = 1
#     cont = int(input('\n[0] - Para finalizar\nInsira o número de termos: '))
# print('--'*25)
# print('Programa finalizado.')

# exercicio 63 - uma forma menor Fibonacci
# cont = int(input('Quantos termos quer ver: '))
# num = 1
# while cont != 0:
#     if cont == 1:
#         print('0')
#         cont -= 1
#     elif cont == 2:
#         print('0 🠖 1')
#         cont -= 2
#     elif cont == 3:
#         print('0 🠖 1 🠖 1')
#         cont -= 3
#     elif cont >= 4:
#         print('0 🠖 1 🠖 1', end='')
#         cont -= 3
#         while cont != 0:
#             calc = 1.618 * num
#             num = round(calc)
#             print(f' 🠖 {round(calc)}', end='')
#             cont -= 1

# melhor solução encontrana na net
# num = 1
# fib = 0
# n = int(input('Digite um número: '))
# while n != 0:
#     print(f'{fib}', end=' → ')
#     fib += num
#     print(n, 'num: ', num, 'fib: ', fib)
#     num = fib - num
#     n -= 1
# print('Fim')

# outra forma
# x, y = 0, 1
# print(0, end=' ')
# while y < 100:
#     print(y, end=' ')
#     x, y = y, x + y


# exercicio 64
# cont = soma = 0
# num = int(input('Digite um número: '))
# while num != 999:
#     soma += num
#     cont += 1
#     num = int(input('Digite um número: '))
# print(f'Quantidade de números digitados {cont}, soma entre os números foi {soma}\nPrograma finalizado')

# exercicio 65
# cont = 0
# soma = 0
# lista = []
# loop = 1
# opc = 's'
# num = float(input('Digite um número: '))
# cont += 1
# soma += num
# lista.append(num)
# while loop == 1:
#     opc = input('''Deseja continuar?
#                 [S] - Sim, continuar
#                 [N] - não continuar
#                 Digite a opção: ''').lower()
#     if opc == 's':
#         num = float(input('Digite um número: '))
#         cont += 1
#         soma += num
#         lista.append(num)
#         loop = 1
#     elif opc == 'n':
#         print(f'A média dos números digitados é {soma / cont:.2f}\nO maior valor é {max(lista):.2f} e o menor {min(lista):.2f}')
#         loop = 0
#     else:
#         print('Opção inválida!')
#         loop = 1
# print('Programa finalizado')

# Aula 15 - break e f strings
# n = s = 0
# while n != 999:
#     s += n
#     n = int(input('Número: ')) # para interromper sem somar, o input pode ir embaixo
# print(f'A some é {s}')

# isso dá pra ser feito utilizando o comando break
# n = s = 0
# while True:
#     n = int(input('Número: '))
#     if n == 999:
#         break
#     s += n
# print(f'A soma é {s}')

# f strings
# nome = 'José'
# idade = 33
# salario = 985.3
# print(f'O {nome:-^10} tem {idade} e ganha R${salario:.2f}') # centralizado com ^
# print(f'O {nome:->10} tem {idade} e ganha R${salario:.2f}') # alinhado a direita >
# print(f'O {nome:-<10} tem {idade} e ganha R${salario:.2f}') # alinhado a esquerda

# exericio 66
# s = 0
# while True:
#     n = int(input('Digite um número: '))
#     if n == 999:
#         break
#     s += n
# print(f'A soma é {s}')

# exercicio 67 - tabuada
# t = ' TABUADA '
# print(f'{t:=^33}')
# while True:
#     n = int(input('[0] - Digite zero para  finalizar\nQuer ver a tabuada de qual número: '))
#     print('--' * 33)
#     if n == 0:
#         break
#     for c in range(1, 11):
#         calc = n * c
#         print(f'{n} X {c} = {calc}')
#     if n != 0: print('--'*33)
# print('Programa finalizado')

# exercicio 68 -  jogo de par ou ímpar
# from random import randint as rd
# cont = 0
# print('{:=^35}'.format(' JOGO PAR OU ÍMPAR '))
# while True:
#     comp = rd(1, 10)
#     esc = int(input('Você quer Par ou Ímpar?\n[0] - Par\n[1] - Ímpar\nEscolha a opção: '))
#     num = int(input('Digite o número: '))
#     print('-'*35)
#     res = (comp + num) % 2
#     if res == esc:
#         print(f'Você jogou {num} e o computador jogou {comp} o total é {comp + num}.\n\033[1;7m Parabéns você venceu! \033[m')
#         cont += 1
#     else:
#         print(f'Você jogou {num} e o computador jogou {comp} o total é {comp + num}.\n\033[1;7m Você perdeu. Game Over! \033[m')
#         break
#     print('-'*35)
# print('-'*35)
# print(f'\033[1;7m Você venceu {cont} vezes. \033[m')

# exercicio 69 - cadastro pessoas
# hom = maior = novinha = cont = 0
# while True:
#     cont += 1
#     print('--'*5, 'Cadastre uma pessoa', '--'*5)
#     idade = int(input('Insira a idade: '))
#     print('-' * 31)
#     sexo = ' '
#     while sexo not in 'mf':
#         sexo = str(input('Insira o sexo\n[M] - Masculino\n[F] - Feminino\nEscolha: '))
#         print('-' * 31)
#     if idade > 18: maior += 1
#     if sexo == 'm': hom += 1
#     if sexo == 'f' and idade < 18: novinha += 1
#     opc = ' '
#     while opc not in 'sn':
#         opc = str(input('Quer continuar?\n[S] - Sim\n[N] - Não\nEscolha: ').lower().strip()[0])
#     if opc == 'n':
#         break
# print('-' * 31)
# print('Programa finalizado')
# print('-' * 31)
# print(f'Total de pessoas cadastradas {cont}')
# print(f'Total de pessoas com mais de 18 anos: {maior}')
# print(f'Ao todo temos {hom} homens cadatrados.')
# print(f'E temos {novinha} mulheres com menos de 18 anos')
# print('-' * 31)

# exercicio 70 - caixa de mercado
# tot = mais = 0
# menor = 100000
# print('{:=^35}'.format(' Loja Super Baratão '))
# while True:
#     nome = input('Nome do produto: ')
#     preco = float(input('Preço R$ '))
#     tot += preco
#     if preco > 1000: mais += 1
#     if preco < menor:
#         menor = preco
#         menor_nome = nome
#     opc = ' '
#     while opc not in 'sn':
#         opc = input('Quer continuar? [S/N] ').lower().strip()[0]
#     if opc == 'n':
#         break
# print('--'*15)
# print(f'O total da compra é R$ {tot}')
# print(f'Temos {mais} custando mais de R$1000,00')
# print(f'O produto mais barato foi {menor_nome} que custa R${menor:.2f}')
# print('--'*15)

# exercicio 71 - Simulador de caixa eletrônico
# print('{:=^35}'.format(' Banco Central '))
# sac = int(input('Quantia a ser sacada R$ '))
# mult = sac // 50
# if mult != 0:
#     sac = sac - (mult * 50)
#     print(f'{mult} cédulas de R$50,00')
# mult = sac // 20
# if mult != 0:
#     sac = sac - (mult * 20)
#     print(f'{mult} cédulas de R$20,00')
# mult = sac // 10
# if mult != 0:
#     sac = sac - (mult * 10)
#     print(f'{mult} cédulas de R$10,00')
# mult = sac // 1
# if mult != 0:
#     sac = sac - (mult * 1)
#     print(f'{mult} cédulas de R$1,00')

# outra forma
# print('{:=^35}'.format(' Banco Central '))
# sac = int(input('Quantia a ser sacada R$ '))
# ced = [50, 20, 10, 1]
# while sac != 0:
#     for c in ced:
#         mult = sac // c
#         if mult != 0:
#             sac = sac - (mult * c)
#             print(f'{mult} cédulas de R${c},00')
# print('-'*35)
# print('Saque seu dinheiro')
