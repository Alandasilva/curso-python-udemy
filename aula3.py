# Verifica se um elemento Ã© membro daquela tipo de dado

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

# Operadores entre valores atribuÃ­dos a variÃ¡veis

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
# o valor do aluguel Ã© o mesmo valor da energia?

print(aluguel is agua)
# o valor do aluguel Ã© o mesmo valor da Ã¡gua?


# Estruturas Condicionais Simples

# IF

nome = input('Digite seu nome:')

if nome == 'Fernando':
    print('Bem-vindo de volta, Fernando!!!')
    
print(f'VocÃª Ã© novo(a) aqui, olÃ¡ {nome}!!!')

# Se a condiÃ§Ã£o for atingida, o bloco Ã© executado,
# caso contrÃ¡rio Ã© simplesmente ignorado


# Estrutura Condicional com Argumento LÃ³gico

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
    print('Você não é Fernando...')
    

# Estrturas Condicionais Aninhadas

num1 = float(input('Digite um número: '))


if num1 <= 50:
    print('Menor que 50')
elif num1 > 50 and num1 < 100:
    print('Maior que 50')
else:
    print('Número Inválido')
    
    

nome1 = 'Fernando'
nome2 = 'Maria'

if nome1 == 'Fernando':
    print('Bem-vindo Fernando!!!')
elif nome2 == 'Maria':
    print('Bem-vinda Maria!!!')
else:
    print('Erro: Nome Desconhecido.')
    
    
# 2 ou mais condições sendo verdadeiras


num1 = 12
num2 = 44
nome1 = 'Fernando'
nome2 = 'Maria'


if num1 >= 10 and nome1 == 'Fernando':
    print('Número maior que 10 e o usuário é Fernando')
if num1 <= 10 and nome1 == 'Fernando':
    print('Número menor que 10 e o usuário é Fernando')
if num1 == num2 and nome2 == 'Maria':
    print('Número 1 e número 2 são iguais, assim como o usuário é Maria')
if num1 != num2 and nome2 == 'Maria':
    print('Número 1 e número 2 são diferentes, assim como o usuário é Maria')

# Operador and exgie que as duas condições sejam verdadeiras (uma condição e outra).


# Estruturas condicionais com interpolação

nomes = ['Fernando', 'Maria', 'Carlos']

usuario = input('Digite seu nome: ')

if usuario in nomes:
    print(f'Bem-vindo(a) {usuario}')
else:
    print('Usuário não cadastrado.')
    
    
# Estruturas Condicionais com Validação Simples (em string)


nome = input('Digite seu nome: ')


if nome == 'Fernando':
    print('Olá Fernando, você é o administrador do sistema!!!')
elif nome in 'Ana Bárbara Carlos José Maria Paulo Tatiana':
    print(f'Bem-vindo(a) {nome}, você é um(a) usuário(a) registrado(a) no sistema')
else:
    print('Olá, você não está logado no sistema, suas permissões são restritas.')
    
    

nome = input('Digite o seu nome: ')


if nome == 'Fernando':
    print('Olá Fernando, você é o administrador do sistema!!!')
elif nome in 'Ana Bárbara Maria Tatiana':
    print(f'Bem vinda {nome}, você é usuária registrada no sistema.')
elif nome in 'Carlos José Paulo':
    print(f'Bem vindo {nome}, você é um usuário registrado no sistema.')
else:
    print('Olá, você não está logado no sistema, suas permissões são restritas.')


nome = input('Digite o seu nome: ')

funcionarios_homens = ['Carlos', 'José', 'Paulo']
funcionarias_mulheres = ['Ana', 'Bárbara', 'Maria', 'Tatiana']


if nome == 'Fernando':
    print('Olá Fernando, você é o administrador do sistema!!!')
elif nome in funcionarias_mulheres:
    print(f'Bem vinda {nome}, você é usuária registrada no sistema.')
elif nome in funcionarios_homens:
    print(f'Bem vindo {nome}, você é um usuário registrado no sistema.')
else:
    print('Olá, você não está logado no sistema, suas permissões são restritas.')

