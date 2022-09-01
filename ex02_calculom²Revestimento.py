l= float(input('Digite a largura da área: '))
largura = l * 100
c = float(input('Digite o comprimento da área: '))
comprimento = c * 100
área = largura * comprimento
print(f'O Tamanho da área é: {c * l}m².')
ceramica = float(input(f'Digite o tamanho(cm) da pedra de cerâmica: '))
rev = ceramica * ceramica
#print(rev)
quant_ceramica = área / rev
#print(quant_ceramica)
preço = float(input('Digite o valor (m²) do revestimento:')) 
preço_final = preço / 10000
preço_ceramica = preço_final * rev
total = preço_ceramica * quant_ceramica
print(f'O custo total do revestimento será: R${total}')
