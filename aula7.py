# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 20:59:40 2022

@author: alans
"""

# Lendo as chaves ou valores por meio de um laço for

d4 = {'1':'A', '2':'B', '3':'C'}

for chaves in d4.keys(): # somente as chaves
    print('Chaves:', chaves)
    
for j in d4.values(): # somente os valores
    print('Valores:', j)
    
for itens in d4.items(): # chaves e valores
    print('Chaves : Valores = ', itens)
    
for n, o in d4.items():
    print(f'Chaves: {n}, Valores: {o}')
    
    
# Listas como valores de uma chave do dicionário

dict = {'almox':['Folha de Oficio','Caneta',
                 'Grampeador'],
        'cozinha':['Café','Açúcar']}

print(dict['almox'][0])

print(dict['cozinha'][1])

# Removendo elementos de um dicionário pela função pop()

dicionario1 = {'Nome':'Fernando',
               'Idade':32,
               'Sexo':'Masculino',
               'Nacionalidade':'Brasileiro'}

dicionario1.pop('Nacionalidade')

print(dicionario1)

# del dicionario1['Nacionalidade']

'''
Mesmo que:
del dicionario1['Nacionalidade']
porém del é uma palavra reservada ao sistema
'''


# Dicionários dentro de dicionários

usuarios = {'João':{'Identificador':'0001',
                    'Cargo':'Porteiro',
                    'Salário':'2000'},
            'Maria':{'Identificador':'0003',
                     'Cargo':'Aux. Limpeza',
                     'Salário':'1900'},
            'José':{'Identificador':'0002',
                    'Cargo':'Técnico',
                    'Salário':'2500'}}

for chaves, valores in usuarios.items():
    print(f'Funcionário: {chaves}')
    
    for i, j in valores.items():
        print(f'\t {i} = {j}')
        


# FUNÇÕES

# Sintaxe básica de uma função

def nome_da_funcao2(parametros):
    "corpo da função"


def minha_funcao():
    print('Minha primeira função personalizada!!!')
    
variavel = minha_funcao()


# Definindo uma função sem parâmetros


def exibe_mensagem():
    print('Seja Bem-Vindo!!!')
    # poderia ser, dependendo o contexto return 'Seja Bem-Vindo!!!'


print(exibe_mensagem())

msg = exibe_mensagem()


# Chamando a função


def mensagem():
    print('Seja Bem Vindo!!!')


mensagem1 = mensagem()

print(mensagem1)



# Criando uma função que temporariamente não faz nada

def funcao():
    pass


var1 = funcao() # não acontecerá nada

print(type(var1)) # Retornará NoneType



# Função interagindo com variável que interage com o usuário


usuario3 = input('Digite o seu nome:')


def mensagem(nome):
    print(f'Bem Vindo {nome}!!!')
    
print(mensagem(usuario3))


# Passando o parâmetro ao chamar a função

def funcao(msg):
    print(msg)
    
funcao('Boas Vindas!!!')   

 
# Exemplo 2


def mensagem(nome):
    print(f'Bem Vindo(a) {nome}!!!!')
    

usuario1 = mensagem('Fernando')


print(usuario1)


# Passando mais de uma parâmetro para uma função


def mensagem(nome, idade):
    print(f'{nome} tem {idade} anos...')
    
usuario1 = mensagem('Fernando', 33)

print(usuario1)


# Definindo parâmetros 'padrão'


def funcao(msg, nome='usuário'):
    print(f'{msg} para {nome}')
    

funcao('Bem vindo')
funcao('Bem vindo','Fernando')


# Passando apenas um parâmetro e recebendo o resto padrão

def funcao(msg='Olá', nome='usuário', msg2='Seja Bem vindo!!!'):
    print(msg, nome, msg2)


funcao(nome='Fernando')


# Passando parâmetro e interagindo com o usuário

def funcao(mensagem, nome='Desconhecido'):
    print(mensagem, nome)
    
funcao('Olá', input('Digite o seu nome: '))    


# Interagindo com o usuário #2

def funcao(msg='Olá', nome='usuário', msg2='Seja Bem Vindo!!!'):
    nome = input('Digite o seu nome: ')
    print(msg, nome, msg2)
    
variavel1 = funcao()    


def funcao(msg='Olá', nome='usuário', msg2='Seja Bem Vindo!!!'):
    return f'{msg} {nome}, {msg2}'

variavel1 = funcao(nome=input('Digite o seu nome: '))

print(variavel1)



# Fazendo operações dentro de uma função


n1 = int(input('Digite o Primeiro Número: '))
n2 = int(input('Digite o Segundo Número: '))
print(f'O resultado da soma é: {n1 + n2}')



def soma(n1, n2):
    return f'O resultado da soma é {n1 + n2}'


n1 = int(input('Digite o Primeiro Número: '))
n2 = int(input('Digite o Segundo Número: '))
print(soma(n1, n2))



# Fazendo operações compostas dentro de uma função


def aumento_percentual(valor, percentual):
    return(valor + (valor * percentual / 100))


num1 = int(input('Digite o valor: '))
num2 = int(input('Você deseja somar quantos % ? '))

calculo = aumento_percentual(num1, num2)



print(f'O valor final será {calculo}')


print(f'O valor final será {round(calculo, 2)} reais')


print(f'O valor final será: R${calculo:.2f} reais.')


# Estruturas condicionais dentro de funções #1

def repetidor(msg):
    contador = 0
    while contador < 5:
        print(msg)
        contador += 1
        
print(repetidor(msg=input('Digite algo para ser repetido 5 vezes: ')))        



# Estruturas condicionais dentro de funções #2

def divisao(n1, n2):
    if n1 == 0 or n2 == 0:
        return 'Operação inválida'
    return n1 / n2

num1 = int(input('Digite o Primeiro Número:'))
num2 = int(input('Digite o Segundo Nümero:'))

print(f'O resultado da divisão é: {divisao(num1, num2)}')


# Estruturas condicionais dentro de funções #3 -
# Fizz Buzz


def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return f'FizzBuzz, {num} é divisível por 3 e por 5'
    if num % 5 == 0:
        return f'Buzz, {num} é divisível por 5'
    if num % 3 == 0:
        return f'Fizz, {num} é divisível por 3'
    return num


print(fizz_buzz(num=int(input('Digite um Número: '))))
