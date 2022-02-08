# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 21:31:51 2022

@author: alans
"""

print(dir())

import builtins

print(dir(builtins))

import random

print(dir(random))


# Definindo parâmetros padrão como False

class Pessoa:
    def __init__(self, nome, idade, sexo=False,
                 altura=False):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura 
        
pessoa1 = Pessoa('Fernando', 33)

print(pessoa1.nome)        

pessoa1.sexo = 'M'

print(pessoa1.sexo)


# Definindo parâmetros como False

class Pessoa:
    def __init__(self, nome, idade, sexo,
                 altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura
        
pessoa1 = Pessoa('Mariana', 2, 'F', 1.76)
print(pessoa1.nome)
print(pessoa1.altura)


pessoa2 = Pessoa('Gilberto', 33, 'M', 1.90)
print(pessoa2.nome)
print(pessoa2.idade)


# Aplicação:
    
class BaseDeDados:
    def __init__(self):
        self.base = {}
        
    def inserir(self, nome, fone):
        if 'clientes' not in self.base:
            self.base['clientes'] = {nome:fone}
        else:
            self.base['clientes'].update({nome:fone})
            
    
    def listar(self):
        for nome, fone in self.base['clientes'].items():
            print(nome, fone)
            
    def apagar(self, nome):
        del self.base['clientes'][nome]
        
clientes = BaseDeDados()

clientes.inserir('Ana', 991358899)
clientes.inserir('Fernando', 981357295)
clientes.inserir('Maria', 999891415)

clientes.listar()

clientes.apagar('Ana')

#clientes.listar()



# @property, Getters e Setters


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco*(percentual/100))
        
        
    #Getter
    @property 
    def preco(self):
        return self._preco
    
    #Setter
    @preco.setter 
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor
        
produto1 = Produto('Camiseta', 99)        
produto1.desconto(5)
print(produto1.preco)


produto2 = Produto('Calça', 'R$59')
produto2.desconto(15)
print(f'Valor de Produto2 com desconto: {produto2.preco}')


# Recursividade

def fatorial(num):
    if num == 1:
        return 1
    
    return num * fatorial(num - 1)

fator = fatorial(int(input('Digite o número a descobrir o fatorial: ')))

print(f'O resultado fatorial é: {fator}')
