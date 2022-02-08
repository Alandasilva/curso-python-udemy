# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 21:01:40 2021

@author: alan silva
"""

# Realizando operações lógicas dentro da função print()

numero = 9


print(numero > 3)

print(numero < 10)

print(numero == 11)

print(numero >= 12)


# Usando fStrings e máscaras de substituição dentro da função print()


nome = 'Fernando'

print(f'Seja muito bem-vindo {nome}!!!')


# Usando operadores por meio de fStrings e suas máscaras de substituição


camisa = 19.90
calca = 39.90

print(f'A soma dos produtos é: {camisa + calca}')


# Sintaxa antiga vs atual moderna

nome = 'Maria'

# Sintaxe funciona básica // Defasada
print('Bem-vindo', nome,'!!!')

# Sintaxe funcional // Defasada
print('Bem-vindo' + ' ' + nome + ' ' '!!!')

# Sintaxe antiga // Defasada
print('Bem-vindo %s !!!'%nome)

# Sintaxe usual // Defasada
print('Bem-vindo {} !!!'.format(nome))

# Sintaxe moderna atual
print(f'Bem-vindo {nome} !!!')
