# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 17:22:08 2021

@author: alans
"""

# Sintaxe básica de uma string

frase1 = 'Atribuido em formato alfanumérico...'
frase2 = "Incluindo números e simbolos!!!"

print(frase1)
print(frase2)

# Contando quantos caracteres compõe uma string


frase1 = 'Porto Alegre é uma cidade brasileira.'

print(len(frase1))



# Contando quantos caracteres compõe uma string


frase1 = str('Porto Alegre é uma cidade Brasileira.')

print(len(frase1))
print(len(frase1) - frase1.count(' '))


# Substituido elementos de uma string

frase1 = 'Porto Alegre é uma cidade Brasileira.'

frase1 = frase1.replace('Porto Alegre', 'Curitiba')

print(frase1)


# Contando caractére específico na string

frase1 = 'Porto Alegre é uma cidade Brasileira.'

print(frase1.count('a'))

# Exibindo a posição do indice de um determinado elemento

print(frase1.find('é'))


# Realizando a leitura de um caractere pelo seu indice

frase1 = 'Porto Alegre é uma cidade Brasileira.'

print(frase1[16])


# Desmembrando uma string, separando cada palavra da frase


frase1 = 'Porto Alegre é uma cidade Brasileira.'

print(frase1.split())


# Concatenando strings por meio de variáveis

mensagem = 'Seja bem-vinda '
usuario = 'Ana Clara'

base = mensagem + usuario

print(base)


# Concatenando diferentes tipos de dados em uma string


nome = 'Ana Clara'
idade = 12


print(f'{nome} tem {idade} anos')

aviso = 'Atenção, geradores entrarão em manutenção às: ' + str(12) + ' horas'

print(aviso)


# Operadores lógicos com uma string

aviso = 'Não é permitida a entrada de menores de 18 anos'

print(aviso)

print('anos' in aviso)

print('gestante' in aviso)


# Letras maiusculas ou minusculas em uma string

alerta = 'Risco de morte'

print(alerta.upper())

print(alerta.lower())


# Convertendo outro tipo de dado para uma string


num1 = 5623
num2 = str(num1)

print(type(num1))
print(type(num2))


# Removendo os espaços no inicio e no fim de uma string 

frase1 = '                 Olá, você é o visitante n 1000  '

print(frase1)
print(frase1.strip())


# Convertendo todas as iniciais das palavras para maiusculo, como um titulo

tema = 'O diganóstico de imagem como ferramenta para detecção de câncer'

tema = tema.title()

print(tema)


# Verificando s uma string é composta por letras e números

variavel = 'aa44'

print(variavel.isalnum()) # Qualquer carctere alganumérico

print(variavel.isalpha()) # Apenas letas

print(variavel.isdigit()) # Apenas numeros


# Pegando dados de uma string e especificando um intervalo

frase1 = 'Porto Alegre é uma cidade Brasileira.'

print(frase1[26:37]) # Intervalo especifico

print(frase1[0:5]) # do início até uma posição

print(frase1[-9]) # de trás pra frente

print(frase1[-11:-1]) 
