# Faça um programa que solicite 3 números inteiros ao usuário 
# e imprime a média aritmética simples e mediana.

mediana = ['','','']
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
media = (num1 + num2 + num3) / 3
sorted
mediana[0] = num1
mediana[1] = num2
mediana[2] = num3
mediana.sort()
print(f'A média aritimética simples é {media:.2f} e a mediana é {mediana[1]}.')