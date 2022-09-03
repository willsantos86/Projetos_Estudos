#Usando 'break' e 'continue'.

while True:
    letra = str(input('Digite uma letra diferente de "X" (Q para sair): '))
    if(letra == 'X'):
        continue
    elif(letra == 'Q'):
        break
    else:
        print(f' A letra digitada foi {letra}.')