#1_Calculo do IRPF

ren_anual = float(input("Qual o valor de seu rendimento bruto anual? "))
if ren_anual < 22847.77:
    aliquota = 0
elif (ren_anual >= 22847.77) and (ren_anual < 33919.81):
    aliquota = 7.5
elif (ren_anual >= 33919.81) and (ren_anual < 45012.61):
    aliquota = 15
elif (ren_anual >= 45012.61) and ( ren_anual< 55976.16):
    aliquota = 22.5
elif (ren_anual >= 55976.16):
    aliquota = 27.5
impostoPagar =  ren_anual * (aliquota / 100)
print('Sua aliquota é de %.2f%% e seu imposto a pagar, R$ %.2f' %(aliquota, impostoPagar))

#2_Calculo do IRPF
ren_anual = float(input("Qual o valor de seu rendimento bruto anual? "))
if ren_anual < 22847.77:
    aliquota = 0
elif 22847.77 <= ren_anual < 33919.81:
    aliquota = 7.5
elif 33919.81 <= ren_anual < 45012.61:
    aliquota = 15
elif 45012.61 <= ren_anual < 55976.16:
    aliquota = 22.5
elif ren_anual <= 55976.16:
    aliquota = 27.5
impostoPagar =  ren_anual * (aliquota / 100)
print('Sua aliquota é de %.2f%% e seu imposto a pagar, R$ %.2f' %(aliquota, impostoPagar))

#3_Calculo do IRPF
ren_anual = float(input("Qual o valor de seu rendimento bruto anual? "))
if ren_anual < 22847.77:
    aliquota = 0
elif ren_anual >= 22847.77:
    if ren_anual < 33919.81:
        aliquota = 7.5
    elif ren_anual >= 33919.81:
        if ren_anual < 45012.61:
            aliquota = 15
        elif ren_anual >= 45012.61:
            if ren_anual< 55976.16:
                aliquota = 22.5
            elif ren_anual >= 55976.16:
                aliquota = 27.5
impostoPagar =  ren_anual * (aliquota / 100)
print('Sua aliquota é de %.2f%% e seu imposto a pagar, R$ %.2f' %(aliquota, impostoPagar))
