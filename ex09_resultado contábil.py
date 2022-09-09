#Resultadso do exercicio.

resultado = float(input('Digite o resultado do exercício:'))
if resultado <= (0-1):
    result = abs(resultado)
    print(f'O resultado do exercício foi: Prejuízo de R${result}')
   
else:
    print(abs(resultado))
    print(f'O resultado do exercíco foi: Lucro de R$ {resultado}')