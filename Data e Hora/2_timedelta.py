from datetime import timedelta, datetime
tipo_carro = 'M'

tempopequeno = 30
tempomedio = 45
tempogrande = 60
data_atual = datetime.now()

if tipo_carro =='P':
    data_estimada = data_atual +timedelta(minutes=tempopequeno)
    print(f'O carro chegou: {data_atual} e ficará pronto: {data_estimada}')
elif tipo_carro =='M':
    data_estimada = data_atual + timedelta(minutes=tempomedio)
    print(f'O carro chegou: {data_atual} e ficará pronto: {data_estimada}')
else:
    data_estimada = data_atual + timedelta(minutes=tempogrande)
    print(f'O carro chegou: {data_atual} e ficará pronto: {data_estimada}')