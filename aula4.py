# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 13:06:05 2021

@author: alans
"""

# Estrutura Condicional composta por or (ou) e and (e)


veiculo1 = 'Gol'
veiculo2 = 'Corsa'
veiculo3 = 'Onibus'
cor1 = 'Branco'
cor2 = 'Vermelho'


if veiculo1 == 'Gol' or veiculo2 == 'Celta':
    print('Carro')
if veiculo1 == 'Gol' and cor1 == 'Branco':
    print('Gol Branco')
if veiculo1 == 'Onibus' and cor2 == 'Vermelho':
    print('Onibus Vermelho')
    
# Condição em or apenas uma das condições precisa ser verdadeira.
# Condição em and as duas condições precisam ser verdadeiras.


# Estrutura de repetição

# WHILE

variavel = 0

while variavel <= 5:
    print(variavel)
    
    variavel = variavel + 1
    


variavel = 0

while variavel <= 5:
    print(variavel)
    
    variavel += 1
    

# Estrutura de Repetição

num = 0
total = 10


while num <= 10:
    print(num)
    num += 1
    
    if num == 5:
        print('50% computado')
        
    if num == total:
        print('100%, processo encerrado')
        
        
# Estrutura de Repetição

validador = input('Digite "Brasil" para continuar:')

while validador != 'Brasil':
    print('Palavra-chave não confere, digite novamente:')
    validador = input('Digite "Brasil" para continuar:')
    
    if validador == 'Brasil':
        print('Agora você digitou Brasil corretamente')
    
    
# Estrutura de Repetição


while True:
    validador = input('Digite "Brasil" para continuar:')
    if validador == 'Brasil':
        print('Você digitou Brasil corretamente!!!')
        break
    else:
        print('Palavra-chave não confere, digite novamente:')
        

# Estruturas de Repetição

# FOR

compras = ['Arroz', 'Feijão', 'Massa', 'Carne', 'Pão']

for i in compras:
    print(i)


# Estrutura de repetição
        
nome = 'Alberto'

for i in nome:
    print(i)
    

# Estrutura de repetição 


for i in range(0,11):
    print(i)

    
# Estruturas de Repetição


vendas = [1000, 459, 911, 838, 50]

total = 0


for i in vendas:
    total += i
    
print(total)    


# Estrutura de repetição

for i in range(0, 11, 2):
    print(i)
    
    

# Estrutura de repetição

for i in range(10, 0, -1):
    print(i)    
    
# Estrutura de repetição

num = int(input('Digite o número limite: '))    

for i in range(0, num+1):
    print(i)
    
# Estrutura de repetição 

nome = 'Fernando'

num = 0

for num in range(len(nome)):
    print(num)
    