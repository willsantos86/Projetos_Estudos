"""Programa de 'Jogo de Forca'. O usuário deverá digitar uma palavra,
 que será a resposta, em seguida, informe ao usuário o tamanho da palavra
 e peça para adivinhar a primeira letra,a segunda etc. até descobrir a 
 palavra ou errar 6 vezes. O jogo acaba quando uma das condições 
 for satisfeita."""     

# %%
tentativa_ok = ''
tentativa_nok = ''
separador = '-'
cont = 1
palavra = input('Digite uma palavra: ')

print(f'Essa palavra tem {len(palavra)} letras!')

while True:
    
    print(f'Tente advinhar a {cont}º letra')
    tentativa = input('Digite uma letra: ')
    if tentativa in palavra:
        cont+=1
    if tentativa in palavra:
        tentativa_ok += tentativa
        print('Acertou!')
    elif tentativa not in palavra:
        tentativa_nok += tentativa
        print(f'Errou! A letra {tentativa} não contém na palavra secreta!')
    if len(tentativa_nok) >= 6:
        print(f'Fim de jogo!! Você esgotou seu número de tentativas!')
        break
    tentativa_ord = list(tentativa_ok)
    tentativa_ord.sort()
    palavra_ord = sorted(palavra)
    if tentativa_ord == palavra_ord:
        print(f'Parabéns, você venceu!! A palavra é {palavra}')
        break

print(f'As letras corretas foram: {separador.join(tentativa_ok)}')
print(f'As letras incorretas foram: {separador.join(tentativa_nok)}')
# %%
