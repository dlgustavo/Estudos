data = input('Informe dia mês e ano separados por / no formato dd/mm/aaaa ')
data_split = data.split("/")
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
mes_indice = data_split[1]
calculo = int(mes_indice) - 1
texto = (data.replace(mes_indice, meses[calculo]))

print(f'{texto.replace('/', ' de ')}')