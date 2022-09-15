#%%
import datetime

hoje = datetime.date.today()
print(f'Hoje é dia {hoje.strftime("%d")}', end='')
print(f"-{hoje.strftime('%m')}", end='')
print(f"-{hoje.strftime('%y')}")
# %%
import time

print(time.time())
print(time.localtime(time.time()))
#agora = datetime.datetime(ano, mês, dia, hora, minuto, segundo, microssegundo,timezone, fold)
data = datetime.date(2022, 9, 14)
hora = datetime.time(10,31,00)
agora = datetime.datetime.now()
print(data)
print(hora)
print(agora)

# %%
print('Usando informações temporais...')
dias = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
agora = datetime.datetime.now()
print(f'Agora são: {agora}')
print('Extraindo os componentes do momento atual:')
print(f'Dia: {agora.day}')
print(f'Mês: {agora.month}')
print(f'Ano: {agora.year}')
print(f'Horas: {agora.hour}')
print(f'Minutos: {agora.minute}')
print(f'Segundos: {agora.second}')
dia_da_semana = datetime.date.weekday(agora)
print(f'Hoje é dia: {dias[dia_da_semana]}, o dia de numero {dia_da_semana + 2} da semana.')
t1 = datetime.datetime(2022,9,6)
t2 = datetime.datetime(2022,9,13)
print(f'A diferença entre {t2} e {t1} é {t2 - t1}')
print('Se você tentar somar duas variáveis datetime, obterá um erro:')
print(t2 + t1)

# %%

