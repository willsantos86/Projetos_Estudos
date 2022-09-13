usuario = input('Digite uma palavra: ')
print(f'Essa palavra tem {len(usuario)} letras!')

cont = 0
while cont <= 6:
    tentativa = input('Digite uma letra: ')
    cont += 1
    for l in usuario:
        if l == tentativa:
            print('Acertou uma letra!')
        
