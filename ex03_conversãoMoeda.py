# Crie um programa que pedirá a cotação do dolar do dia, uma quantidade de reais
# e exibirá o valor convertido para dólares.

dolar = float(input('Digite a cotação do dolar: '))
real = float(input('Digite o valor (R$) a ser convertido: '))
conversao = real / dolar
print(f'O valor de R${real} equivale a US${conversao:.2f}.')