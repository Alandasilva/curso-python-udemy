# Verifica se um elemento é membro daquela tipo de dado

lista = [1, 2, 3, 'Ana', 'Maria']

print(2 in lista)
print('Maria' in lista)
print('Carlos' in lista)

# Maior que

idade = 12

print(idade > 4)

# Maior ou igual que

num1 = 7

print(num1 >= 7)

# Operadores entre valores atribuídos a variáveis

x = 2
z = 5

print(x > z)
print(x >= z)

y = 7
z = 5

print(z <= y)


x = 2
z = 7

print(x is 2 and y != x)

x = 9
print(x is 2 and y != x)


aluguel = 250
energia = 250
agua = 65

print(aluguel is energia)
# o valor do aluguel é o mesmo valor da energia?

print(aluguel is agua)
# o valor do aluguel é o mesmo valor da água?


# Estruturas Condicionais Simples

# IF

nome = input('Digite seu nome:')

if nome == 'Fernando':
    print('Bem-vindo de volta, Fernando!!!')
    
print(f'Você é novo(a) aqui, olá {nome}!!!')

# Se a condição for atingida, o bloco é executado,
# caso contrário é simplesmente ignorado


# Estrutura Condicional com Argumento Lógico

num = 49

if num < 50:
    print('Menor que 50')
else:
    print('Maior que 50')


# Estruturas Condicionais Compostas


nome = input('Digite seu nome:')

if nome == 'Fernando':
    print('Bem-vindo de volta, Fernando!!!')
else:
    print('Voc� n�o � Fernando...')
    

# Estrturas Condicionais Aninhadas

num1 = float(input('Digite um n�mero: '))


if num1 <= 50:
    print('Menor que 50')
elif num1 > 50 and num1 < 100:
    print('Maior que 50')
else:
    print('N�mero Inv�lido')
    
    

nome1 = 'Fernando'
nome2 = 'Maria'

if nome1 == 'Fernando':
    print('Bem-vindo Fernando!!!')
elif nome2 == 'Maria':
    print('Bem-vinda Maria!!!')
else:
    print('Erro: Nome Desconhecido.')
    
    
# 2 ou mais condi��es sendo verdadeiras


num1 = 12
num2 = 44
nome1 = 'Fernando'
nome2 = 'Maria'


if num1 >= 10 and nome1 == 'Fernando':
    print('N�mero maior que 10 e o usu�rio � Fernando')
if num1 <= 10 and nome1 == 'Fernando':
    print('N�mero menor que 10 e o usu�rio � Fernando')
if num1 == num2 and nome2 == 'Maria':
    print('N�mero 1 e n�mero 2 s�o iguais, assim como o usu�rio � Maria')
if num1 != num2 and nome2 == 'Maria':
    print('N�mero 1 e n�mero 2 s�o diferentes, assim como o usu�rio � Maria')

# Operador and exgie que as duas condi��es sejam verdadeiras (uma condi��o e outra).


# Estruturas condicionais com interpola��o

nomes = ['Fernando', 'Maria', 'Carlos']

usuario = input('Digite seu nome: ')

if usuario in nomes:
    print(f'Bem-vindo(a) {usuario}')
else:
    print('Usu�rio n�o cadastrado.')
    
    
# Estruturas Condicionais com Valida��o Simples (em string)


nome = input('Digite seu nome: ')


if nome == 'Fernando':
    print('Ol� Fernando, voc� � o administrador do sistema!!!')
elif nome in 'Ana B�rbara Carlos Jos� Maria Paulo Tatiana':
    print(f'Bem-vindo(a) {nome}, voc� � um(a) usu�rio(a) registrado(a) no sistema')
else:
    print('Ol�, voc� n�o est� logado no sistema, suas permiss�es s�o restritas.')
    
    

nome = input('Digite o seu nome: ')


if nome == 'Fernando':
    print('Ol� Fernando, voc� � o administrador do sistema!!!')
elif nome in 'Ana B�rbara Maria Tatiana':
    print(f'Bem vinda {nome}, voc� � usu�ria registrada no sistema.')
elif nome in 'Carlos Jos� Paulo':
    print(f'Bem vindo {nome}, voc� � um usu�rio registrado no sistema.')
else:
    print('Ol�, voc� n�o est� logado no sistema, suas permiss�es s�o restritas.')


nome = input('Digite o seu nome: ')

funcionarios_homens = ['Carlos', 'Jos�', 'Paulo']
funcionarias_mulheres = ['Ana', 'B�rbara', 'Maria', 'Tatiana']


if nome == 'Fernando':
    print('Ol� Fernando, voc� � o administrador do sistema!!!')
elif nome in funcionarias_mulheres:
    print(f'Bem vinda {nome}, voc� � usu�ria registrada no sistema.')
elif nome in funcionarios_homens:
    print(f'Bem vindo {nome}, voc� � um usu�rio registrado no sistema.')
else:
    print('Ol�, voc� n�o est� logado no sistema, suas permiss�es s�o restritas.')

