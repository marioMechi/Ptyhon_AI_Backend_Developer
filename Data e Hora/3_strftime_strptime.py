from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str ='2013-10-05 10:20'
mascara_ptbr = '%d/%m/%Y'
mascara_en = '%Y-%m-%d %H:%M'

print(data_hora_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(data_hora_str, mascara_en)

print(type(data_convertida), data_convertida)


