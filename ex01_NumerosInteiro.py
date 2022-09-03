#Crie um programa que receba números inteiros e os imprima na ordem inversa
#em que foram digitados.Dica:aramazene os números em uma lista.

#Solução1
numeros = ['','','','','']
num1 = int(input('Digite o primeiro número inteiro: '))
numeros[4] = num1 
num2 = int(input('Digite o segundo número inteiro: '))
numeros[3] = num2 
num3 = int(input('Digite o terceiro número inteiro: '))
numeros[2] = num3
num4 = int(input('Digite o quarto número inteiro: '))
numeros[1] = num4 
num5 = int(input('Digite o quinto número inteiro: '))
numeros[0] = num5

print(f'{numeros}')

#Solução2
numeros = ['','','','','']
num1 = int(input('Digite o primeiro número inteiro: '))
numeros[0] = num1 
num2 = int(input('Digite o segundo número inteiro: '))
numeros[1] = num2 
num3 = int(input('Digite o terceiro número inteiro: '))
numeros[2] = num3
num4 = int(input('Digite o quarto número inteiro: '))
numeros[3] = num4 
num5 = int(input('Digite o quinto número inteiro: '))
numeros[4] = num5

print(numeros[4],numeros[3],numeros[2], numeros[1], numeros[0])