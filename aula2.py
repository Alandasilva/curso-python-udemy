# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 13:27:55 2021

@author: alans
"""

nome = input('Digite o seu nome: ')


print(nome)
print(f'Bem vindo {nome}!')


# Soma

print(5 + 7)

# Subtração

print(12 - 3)

# Multiplicação

print(5 * 7)

# Dvisão

print(120 / 7)


print(5 + 2 * 7)

print((5 + 2) * 7)

# potenciação

print( 3 ** 5)

# divisão exata

print(9.4 // 3) # sem considerar o resto

# Módulo/Resto de uma dvisão

print( 10 % 3 )


# Atribuindo um dado ou valor a uma variável

nome = 'Fernando'
idade = 33

# Atribuição aditiva

valor = 4

valor = valor + 5


print(valor)

# Atribuição subtrativa

valor = 4

valor = valor - 3


print(valor)

# Atribuição multiplicativa

valor = 4

valor = valor * 3
valor *= 3 # outra forma

print(valor)


# Atribuição divisiva

valor = 12

valor = valor / 2
valor /= 2 # outra forma

print(valor)

# Moódulo de (ou resto da divisão de)

valor = 12

valor = valor % 4
valor %= 4

print(valor)


# Divisão inteira

valor = 512

valor = valor // 256

print(valor)


# Exponenciação

valor = 4


valor = valor ** 8
valor **= 8 # outra forma

print(valor)


equacao = ((50 + 25) * 7.2) / 3.8

print(f'O resultado bruto da equação é: {equacao}')

print(f'O resultado bruto da equação é: {equacao:.2f}')

print(f'O resultado é: {round(equacao, 5)}')


# Igualdade

print(5 == 6)

print(12 == 12)


# Diferença


print(7 != 3)

# Operadores lógicos compostos
# Todas as condições precisam ser verdadeiras para True

print(7 != 3 and 2 > 3)

num1 = 4
num2 = 9
num3 = 9

print(num1 == num2)
print(num1 is num2)

print(num2 is 9)

print(num2 is num3)
