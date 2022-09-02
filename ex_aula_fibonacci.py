'''Sequencia de Fobonacci.'''


n = int(input('Quantos números da sequencia de Fibonacci você quer ver? '))
contador = 0
x1 = 1
x2 = 1
fib_n = 0
while (contador <= n):
    contador += 1
    fib_n = x1 + x2
    x1 = x2
    x2 = fib_n
    print(fib_n)

#%%
alunos =['Alice', 'Bob', 'Carl', 'Daniele']
notas = [9.5, 8.0, 9.5, 8.0]

for indice, aluno in enumerate(alunos):
    print(f'Nome:{aluno} - Nota: {notas[indice]}')
# %%



# %%
