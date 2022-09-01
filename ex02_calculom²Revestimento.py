# Escreva um programa que solicite as dimensões (largura e o comprimento) de uma sala
# em metros, o tamanho da aresta de uma peça quadrada de cerâmica em cm e o preço do m²
# da referida cerâmica;imprima quantos m² devem ser adquiridos para pavimentar a referida
# sala e descubra quanto custará a cerâmica a ser usada.


l= float(input('Digite a largura da área: '))
largura = l * 100
c = float(input('Digite o comprimento da área: '))
comprimento = c * 100
área = largura * comprimento
print(f'O Tamanho da área é: {c * l}m².')
tam_peça= float(input(f'Digite o tamanho(cm) da pedra de cerâmica: '))
tam_rev = tam_peça * tam_peça
quant_ceramica = área / tam_rev
preço_peça = float(input('Digite o valor (m²) do revestimento:')) 
preço_final = preço_peça/ 10000
preço_tot_ceramica = preço_final * tam_rev
total = preço_tot_ceramica * quant_ceramica

print(f'O custo total do revestimento será: R${total}')
