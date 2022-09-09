#Crie um programa que solicite ao usuário que digite seu login e , em seguida
#Verifica se esse login está de acordo com as seguintes regras.

#Inicia com uma letra maiúscula.
#Tem, no mínimo,seis caracteres.
#Possui, pelo menos, dois caracteres numéricos.
#Possui, pelo menos, três letras.
#Possui tamanho dde até dez caracteres.



login_ok = True
numeros = 0
letras = 0
login = input('Digite seu login: ')
padrão = login.capitalize()

if login != padrão:
    login_ok = False
    print('O login deve iniciar com uma letra maiúscula!')
elif len(login) < 6:
    login_ok = False
    print('O login deve possuir, no mínimo, 6 caracteres!')

for letra in login:
    if letra.isdigit():
        numeros += 1
    if letra.isalpha():
        letras += 1
if letras < 3:
    login_ok = False
    print('O login deve possuir, no mínimo, 3 letras!')
if numeros < 2:
    login_ok = False
    print('O login deve possuir, no mínimo, 2 caractéres numéricos!')
if len(login) > 10:
    login_ok = False
    print('O login deve possuir, no máximo, 10 caracteres! ')
if login_ok:
    print(f'O login escolhido, {login}, é válido!')


