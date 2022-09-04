import math

print(abs(500))
print(abs(-500))
print(math.ceil(5.5632))
print(math.floor(5.5632))
print(math.pow(7,8))

import random

string = 'abacate laranja tomate'
print(random.choice(string))
lista = ['abacate','laranja', 'tomate']
print(random.choice(lista))
tupla = ('abacate', 'laranja', 'tomate')
print(random.choice(tupla))

print(random.randrange(1,10))
print(random.choice(range(1,10)))

nomes = ['Alice', 'Bob', 'Carl', 'Daniele', 'Edgard']
for n in range(5):
    random.shuffle(nomes)
    print(f'Na passagem de número {n +1} a lista estava assim: {nomes}')

nomes = ['Alice', 'Bob', 'Carl', 'Daniele', 'Edgard']
for n in range(5):
    nomes: random.sample(nomes, k = len(nomes))
    print(f'Na passagem de número {n + 1} a tupla estava assim:{nomes}')

tupla = (1, 2, 3, 4)
print(tupla)