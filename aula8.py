# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 16:05:56 2022

@author: alans
"""

# Função com argumentos externos


def funcao(*args):
    for parametro in args:
        print(parametro)
        
argumentos = ('nome', 'idade')        

funcao(argumentos)

# Desempacotando uma lista para que os elementos dela virem argumentos


lista1 = ['nome', 'idade', 'sexo', 'nacionalidade']


def funcao(*args):
    print('Informações Necessárias')
    print(args)
    
    
funcao(*lista1)    


# Função com parâmetros baseados em *args e **kwargs

# Supondo que está cadastrando senhas e usuários em um sistema

def funcao(*args, **kwargs):
    print(args)
    print(kwargs)
    
senhas_padrao = [12345, 11111, 54321]

resultado = funcao(*senhas_padrao, usuario='user', administrador='admin')


print(resultado)   


# Função com parâmetros baseados em *args e **kwargs

# Buscando dados do modelo anterior

def funcao(*args, **kwargs):
    nome = kwargs['usuario']
    nome2 = kwargs['administrador']
    senha1 = args[0]
    senha2 = args[1]
    
    print(f'O usuário padrão é: {nome}')
    print(f'O administrador é: {nome2}')
    print(f'A senha padrão é: {senha1}')
    print(f'A senha alternativa é: {senha2}')


senha_padrao = [12345, 11111]


funcao(*senhas_padrao, usuario='user', administrador='admin')



# FUnção que recebe outra função como parâmetro


def mestre(funcao):
    return funcao()

def msg_boas_vindas():
    return 'Seja Muito Bem Vindo!!!'


executa = mestre(msg_boas_vindas)

print(executa)


# Expressões Lambda / funções vazias

def multiplicador(num1, num2):
    return num1 * num2

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
variavel1 = multiplicador(num1, num2)

print(variavel1)


num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

variavel2 = lambda num1, num2: num1 * num2

print(variavel2(num1,num2))



# Escopo Global vs Escopo Local

variavel1 = 'Paulo'

def funcao1():
    print(f'Print da variável do escopo global: {variavel1}')
    
funcao1()


def funcao2():
    variavel2 = 'Maria'
    print(f'Print da variável do escopo local: {variavel2}')
    
funcao2()  


# Modificando uma variável global de dentro de uma função

num1 = 100

print(f'Variável com seu valor inicial: {num1}') 


def modificador():
    global num1
    num1 = 200
    print(f'Variável alterada dentro da função: {num1}')
    
modificador()


print(f'Variável atualizada pela função modificador: {num1}')


# Sintaxe básica usual

# POO
  
# Criando uma classe vazia


class Pessoa:   
    pass    

# Criando objetos (atribuidos de classe) dentro de uma classe

class Pessoa:
    pass

pessoa1 = Pessoa()

pessoa1.nome = 'Fernando'
pessoa1.idade = 32

print(pessoa1.nome)
print(pessoa1.idade)


# Criando funções (métodos de classe) dentro de uma classe

class Pessoa:
    def acao1(self):
        print('Ação 1 sendo executada...')
        
        
pessoa1 = Pessoa()        


pessoa1.acao1()


# Criando uma classe com método construtor e objetos internos

class Pessoa:
    def __init__(self, nome, idade, sexo, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura
        
        
pessoa1 = Pessoa('Fernando', 32, 'M', 1.90)


print(pessoa1.nome, pessoa1.idade)        
print(f'Bem vindo {pessoa1.nome}, parabéns pelos seus {pessoa1.idade} anos!!!')


# Mais de um método de classe dentro de uma classe

class Pessoa:
    ano_atual = 2022
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def ano_nascimento(self):
        ano_nasc = self.ano_atual - self.idade
        print(f'Seu ano de nascimento é {ano_nasc}')
        
pessoa1 = Pessoa('Fernando', 32)
pessoa2 = Pessoa('Alan', 25)     

print(pessoa1.ano_nascimento())
print(pessoa2.ano_nascimento())



# Métodos que até interagem com funções internas,
# mas retorna dados para o escopo global de classe.


class Pessoa:
    ano_atual = 2022
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    @classmethod
    def ano_nasc(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    
pessoa2 = Pessoa.ano_nasc('Fernando', 1987)

print(pessoa2.idade)



# Métodos estáticos

# Aqueles que não possuem instâncias como atributos,
# funciona como uma função normal dentro da classe


from random import randint


class Pessoa:
    @staticmethod 
    def gerador_id():
        gerador = randint(100, 999)
        return gerador
    
print(Pessoa.gerador_id())


# Atributos de classe


class Classe1:
    var1 = 101001


variavel1 = Classe1()


print(Classe1.var1)

print(variavel1.var1)


# Mudando um atributo de classe

class Classe1:
    var1 = 101001
    
variavel1 = Classe1()

Classe1.var1 = 'Maria'    

print(Classe1.var1)



# Encapsulamento


class BaseDeDados:
    def __init__(self):
        self.dados = {}
        #self._dados = {}
        # declarado como protegido (ainda acessével de fora da classe)
        
        #self.__dados = {}
        # declarado como privado (inacessível e imutável de fora da classe)
        
        
base = BaseDeDados()        

print(base.dados)


# Try, Except

try:
    print(variavel)
except:
    pass

# Exibindo que erro específico ocorreu

try:
    print(var)
except:
    print('A variável Não Existe!!!')
    
    
# Exibindo que erro aconteceu

try:
    print(a)
except NameError as erro:
    print('Ocorreu um erro:', erro)
    
    
# Except genérico:
except Exception as erro:
    print('Ocorreu um erro inesperado', erro)
    
    
# Modularização básica

def soma(num1, num2):
    s = int(num1) + int(num2)
    return s

import aula9

print(f'O resultado da soma é: {aula9.soma(123,3)}')


# Modularização básica

from aula9 import soma

print(f'O resultado da soma é: {soma(999,3)}')
