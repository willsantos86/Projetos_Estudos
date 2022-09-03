# Média da turma.

nomes = ['','','','','']
notas = [0.0, 0.0, 0.0, 0.0, 0.0]
for contador in range(5):
    print(f'Entre com nome de aluno {contador + 1}: ')
    nomes[contador] = input()
    print(f'Entre com a nota de {nomes[contador]}: ')
    notas[contador] = float(input())
    notas.sort(reverse=True)
print(notas)