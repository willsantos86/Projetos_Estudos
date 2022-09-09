#Crie um jogo eletronico, em que o usuário irá apostar em um número de 1 a 100 
# e o computador sorteará um numero inteiro. Se corresponder ao que o usuário digitou, ele imprimirá
#"Você venceu!", se não, mostrará "A banca sempre ganha!"

import random

computador = random.randrange(1,100,1)
jogador = int(input('Escolha e digite um valor de 1 a 100: '))

if computador ==  jogador:
    print(f'Você venceu!\nVocê e o computador escolheram o número {jogador}')
else:
    print(f'''A Banca sempre ganha!!\nVocê escolheu o número {jogador}, mas o computador escolheu o número {computador}''')