'''Faça um programa que receba o comprimento do cateto oposto
 e do cateto adjacente de um triãngulo retãngulo, 
calcule e mostre o comprimento da hipotenusa'''

a = float(input('Digite o lado A do triângulo: '))
b = float(input('Digite o lado B do triângulo: '))
c = (a*a + b*b) ** 0.5

print(f'A hipotenusa vai medir {c:.2f}')

if (a + b) >= c:
    print('É possível formar um triângulo')

else:
    print('Não é possível formar um triângulo!')
