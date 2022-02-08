# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 12:48:54 2021

@author: alans
"""

'''
Lembrar que o índice de uma lista começa do 0 (zero)!
'''

# Criando listas simples

lista1 = ['Ana Clara', 'Carlos', 19.99, 'Michele', 'Fernando', 1987]

print(lista1)

# Descobrindo um elemento de uma lista através de seu indice

lista1 = ['Ana Clara', 'Carlos', 'Michele', 'Fernando', 1987]

print(lista1[3])

# Descobrindo um número de um índice através de um determinado elemento

print(lista1.index('Michele'))

# Descobrindo o número de elementos de uma lista

print(len(lista1))


# Adicionando um novo elemento a uma lista

lista1.append('Paulo')
lista1.append(9999999)

print(lista1)


# Substituindo um novo elemento em uma posição específica

lista1 = ['Ana Clara', 'Carlos', 'Michele', 'Fernando', 1987]

lista1[2] = 'José'
lista1[4] = 99999
print(lista1)


# Adicionando um novo elemento em uma lista em uma posição específica


lista1 = ['Ana Clara', 'Carlos', 'Michele', 'Fernando', 1987]

lista1.insert(2, 'José')

print(lista1)


# Removendo um elemento em uma lista em uma posição específica


lista1 = ['Ana Clara', 'Carlos', 'Michele', 'Fernando', 1987]

lista1.remove(lista1[4])

print(lista1)


# Listas dentro de listas


cadastro = [1, 2, 3, 4, ['Ana', 'Maria', 'Paulo', 'Roberto']]

print(cadastro)
print(cadastro[4])


# Laço de repetição for


repetir = 's'
fatura = []
total = 0

while repetir == 's':
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço: '))
    
    fatura.append([produto, preco])
    total += preco
    
    repetir = input('Cadastrar mais algum item? (S ou N)').lower()
    
    
for i in fatura:
    print(i[0], ':', i[1])
    
    
print('O total da fatura é: ', total)


# Criando um conjunto numérico (set) em Python

# SET

conjunto1 = {5, 10, 15, 20}

print(type(conjunto1))


# Operações entre conjuntos

cj1 = {1, 2, 3, 4, 5}

cj2 = {1, 3, 5, 7, 9}

print(cj1 - cj2)


# União de conjuntos numéricos

conjunto1 = {5, 10, 15, 20}

conjunto2 = {1, 2, 3, 4, 5}

uniao = conjunto1.union(conjunto2)


print(uniao)


# Interseção de conjuntos


conjunto1 = {5, 10, 15, 20}

conjunto2 = {1, 2, 3, 4, 5}

intersecao = conjunto1.intersection(conjunto2)


print(intersecao)


# Operadores lógicos em conjuntos numéricos

conjunto1 = {5, 10, 15, 20}

conjunto2 = {1, 2, 3, 4, 5}

uniao = conjunto1.union(conjunto2)


print(uniao == conjunto1)

print(uniao >= conjunto2)


# Diferença entre conjuntos

c1 = {1, 2, 3, 4, 5} - {1, 2}

print(c1)


# Diferença entre conjuntos associados a variáveis

c1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
c2 = {1, 3, 5, 7 ,9}


print(c1 - c2)

# ou 

dif = c1 - c2
print(dif)


# Pilhas

sequencia = [11, 22, 33, 444]

pilha = []

for elemento in sequencia:
    pilha.append(elemento)
    

pilha.append(555)
pilha.pop() 


while len(pilha) > 0:
    print(pilha)
    
    topo = pilha.pop()
    
    print(f'Objeto do topo da pilha: {topo}')
    
    
    
# Uso de máscaras de substituição
# Interpolação


nome = 'Maria'
exp = 33

print(f'Olá {nome}, queremos te parabenizar por seus {exp} anos em nossa empresa.')


# Operações dentro de máscaras de substituição

nome = 'Maria'
idade = 30

print(f'{nome} tem 3 vezes minha idade, ela tem {3 * idade} anos!!!')


# Sintaxe básica de um dicionário

dicionario = {'chave': 'valor'}


print(dicionario)


# Adicionando novos elementos ao dicionario


dicionario1 = {'Nome1': 'Paulo'}

print(dicionario1)


dicionario1['Nome2'] = 'Veronica'

print(dicionario1)


# Alterando o valor de uma chave do dicionário

dicionario1 = {'Nome1': 'Ana',
               'Nome2': 'Carla',
               'Nome3': 'Maria'}

print(dicionario1)


dicionario1['Nome2'] = 'Bárbara'

print(dicionario1)


# Acessando um elemento do dicionário

dicionario1 = {'Nome':'Fernando',
               'Idade':32,
               'Sexo':'Masculino',
               'Nacionalidade':'Brasileira'}


print(dicionario1['Nome'])

print(dicionario1['Nacionalidade'])


# Usando o construtor de dicionários do Python


dicionario2 = dict(chave1 = 'valor da chave1',
                   chave2 = 'valor da chave2')

print(dicionario2)

print(type(dicionario2))


# Consultando apenas as chaves de um dicionario


dicionario2 = dict(chave1 = 'valor da chave1',
                   chave2 = 'valor da chave2')

print(dicionario2.keys())


# Consultando apenas os valores de um dicionario


dicionario2 = dict(chave1 = 'valor da chave1',
                   chave2 = 'valor da chave2')

print(dicionario2.values())


# Verificando se uma chave ou valor consta em um 
# dicionario

d3 = {'1':'Ana',
      '2':'Maria',
      '3':'Paulo',
      '4':'Marcos'}


print(d3.get('5'))

print(d3.get('2'))


# Verificando se uma chave ou valor consta em um 
# dicionario

# Pesquisando pela chave, obtendo o valor

print('3' in d3)

print('2' in d3.keys())

print('Ana' in d3.values())

print(d3['2'] == 'Maria')

# Atualizando um elemento do dicionário

d4 = {'1':'A',
      '2':'B',
      '3':'C',
      '4':'D'}

print(d4)

d4.update({'2': 'E'})

print(d4)

# Removendo um elemento do dicionário


d4 = {'1':'A',
      '2':'B',
      '3':'C',
      '4':'D'}

del d4['4']

print(d4)


# Imprimindo só chaves e só valores

d4 = {'1':'A', '2':'B', '3':'C', '4':'D',
      '5':'E', '6':'F'}

print(d4.keys())

print(d4.values())


# Pesquisando o tamanho de um dicionário

print(len(d4))
