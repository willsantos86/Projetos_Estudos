#Crie um programa que solicite ao usuário que digite seu login e , em seguida
#Verifica se esse login está de acordo com as seguintes regras.

#Inicia com uma letra maiúscula.
#Tem, no mínimo,seis caracteres.
#Possui, pelo menos, dois caracteres numéricos.
#Possui, pelo menos, três letras.
#Possui tamanho de até dez caracteres.
login_ok = True
letras = 0
numero = 0
ok = []
nok = []
separador = '#'

while True:
    login = input('Digite seu login: ')
    if login != login.capitalize():
        login_ok = False
        print('O login deve começar com letra MAIÚSCULA!')
    if len(login) < 6:
        login_ok = False
        print('O login deve ter, no mínimo, 6 caracteres!')
    

    for letra in login:
        if letra.isnumeric():
            numero += 1
        if letra.isalpha():
            letras += 1
    if numero < 2:
        login_ok = False
        print('O login deve possuir, no mínimo, 2 caracteres numérico!')
    if letras < 3:
        login_ok = False
        print('O login deve possuir, no mínimo, 3 letras!')
    if len(login) > 10:
        login_ok = False
        print('O login deve ter, no máximo, 10 caracteres!')
    if login_ok:
        ok.append(login)
        print(separador.join(ok))
    if login_ok == False:
        nok.append(login)
    print(f'Esses são os logins não aceitos! {separador.join(nok)}')



    resp = str(input('Deseja incluir outro login: ')).upper()
    if resp != 'S':
        break




