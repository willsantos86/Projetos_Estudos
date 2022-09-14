#%%
tentativa_ok = ''
tentativa_nok = ''
palavra = input('Digite uma palavra: ')
print(f'Essa palavra tem {len(palavra)} letras!')


while True:
    tentativa = input('Digite uma letra: ')

    for l in palavra:
        if l == tentativa:
            tentativa_ok += tentativa
            print('Acertou!')
        elif l != tentativa:
            tentativa_nok += tentativa
            print(f'Errou! A letra {tentativa} não contém na palavra secreta!')
    if len(tentativa_nok) >= 6:
        print(f'Fim de jogo!! Você esgotou seu número de tentativas!')
        break
    if tentativa_ok == palavra:
        print(f'Parabéns, você venceu!! A palavra é {palavra}')
        break


        
# %%
tentativa_ok = ''
tentativa_nok = ''
palavra = input('Digite uma palavra: ')
print(f'Essa palavra tem {len(palavra)} letras!')


while True:
    tentativa = input('Digite uma letra: ')
   
    if tentativa in palavra:
        tentativa_ok += tentativa
        print('Acertou!')
    elif tentativa not in palavra:
        tentativa_nok += tentativa
        print(f'Errou! A letra {tentativa} não contém na palavra secreta!')
    if len(tentativa_nok) >= 6:
        print(f'Fim de jogo!! Você esgotou seu número de tentativas!')
        break
    if tentativa_ok == palavra:
        print(f'Parabéns, você venceu!! A palavra é {palavra}')
        break
# %%
