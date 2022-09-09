#Crie um programa de 'Jogo de Dados': dois usuários devem fornecer seus nomes
#e o programa sorteará números entre 1 e 6 (inclusive) para cada jogador, informando,
#a seguir, o resultado (quem venceu e qual o placar).


import random

jogador1 = str(input('Digite o nome do primeiro jogador: '))
jogador2 = str(input('Digite o nome do segundo jogador: '))
computador1 = random.randrange(1,7)
computador2 = random.randrange(1,7)

if computador1 > computador2:
    print(f'O VENCEDOR foi {jogador1}')
elif computador1 < computador2:
    print(F'O VENCEDOR foi {jogador2}')
else:
    print('Não houve VENCEDOR! Os números sorteados foram iguais!!')
print(f'O número sorteado para {jogador1} foi {computador1}')
print(f'O número sorteado para {jogador2} foi {computador2}')

