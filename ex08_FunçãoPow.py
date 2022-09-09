#Crie um programa que solicite as cordenadas de (x,y,z) de três pontos no espaço em três dimensões
#e mostrará na saída se esses pontos formam ou não um triângulo.
import math


x = [['',''], ['',''], ['','']]
y = [['',''], ['',''], ['','']]
z = [['',''], ['',''], ['','']]

x[0][0] = int(input('Digite a cordenada "X[0][0]": '))
x[0][1] = int(input('Digite a cordenada "X[0][1]": '))
x[1][0] = int(input('Digite a cordenada "X[1][0]": '))
x[1][1] = int(input('Digite a cordenada "X[1][1]": '))
x[2][0] = int(input('Digite a cordenada "X[2][0]": '))
x[2][1] = int(input('Digite a cordenada "X[2][1]": '))
y[0][0] = int(input('Digite a cordenada "Y[0][0]": '))
y[0][1] = int(input('Digite a cordenada "Y[0][1]": '))
y[1][0] = int(input('Digite a cordenada "Y[1][0]": '))
y[1][1] = int(input('Digite a cordenada "Y[1][1]": '))
y[2][0] = int(input('Digite a cordenada "Y[2][0]": '))
y[2][1] = int(input('Digite a cordenada "Y[2][1]": '))
z[0][0] = int(input('Digite a cordenada "Z[0][0]": '))
z[0][1] = int(input('Digite a cordenada "Z[0][1]": '))
z[1][0] = int(input('Digite a cordenada "Z[1][0]": '))
z[1][1] = int(input('Digite a cordenada "Z[1][1]": '))
z[2][0] = int(input('Digite a cordenada "Z[2][0]": '))
z[2][1] = int(input('Digite a cordenada "Z[2][1]": '))

print(x,y,z)

p1 = math.sqrt(pow(x[0][1]-x[0][0],2) + pow(y[0][1]- y[0][0],2) + pow(z[0][1]- z[0][0],2)) 
p2 = math.sqrt(pow(x[1][1]-x[1][0],2) + pow(y[1][1]- y[1][0],2) + pow(z[1][1]- z[1][0],2))
p3 = math.sqrt(pow(x[2][1]-x[2][0],2) + pow(y[2][1]- y[2][0],2) + pow(z[2][1]- z[2][0],2))
p1 = p1.real
p2 = p2.real
p3 = p3.real
print(f'{p1:.2f}, {p2:.2f}, {p3:.2f}')

#lado1 = float(input('Entre com o tamanho do primeiro seguimento:'))
#lado2 = float(input('Entre com o tamanho do segundo seguimento:'))
#lado3 = float(input('Entre com o tamanho do terceiro seguimento:'))
#forma_triangulo = False
if (p1 <= p2 + p3) and (p2 <= p1 + p3) and (p3 <= p1 +p2):
    print('Forma triângulo')   
else:
    print(f'Os seguimentos NÃO formam triângulo algum.')
