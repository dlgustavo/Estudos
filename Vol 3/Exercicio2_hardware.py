valor_pagar = int(input('Informe o valor a pagar'))
valor_pago = int(input('Informe o valor pago'))
troco = valor_pago - valor_pagar
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
nota1 = 0

while troco >= 50:
    troco = troco - 50
    nota50 = nota50 + 1
while troco >= 20:
    troco = troco - 20
    nota20 = nota20 + 1
while troco >= 10:
    troco = troco - 10
    nota10 = nota10 + 1
while troco >= 5:
    troco = troco - 5
    nota5 = nota5 + 1
while troco >= 2:
    troco = troco - 2
    nota2 = nota2 + 1
while troco >= 1:
    troco = troco - 1
    nota1 = nota1 + 1
if troco == 0:
 
    texto = f'''
A quantidade de notas de 50 recebidas seriam {nota50}
A quantidade de notas de 20 recebidas seriam {nota20}
A quantidade de notas de 10 recebidas seriam {nota10}
A quantidade de notas de 5 recebidas seriam {nota5}
A quantidade de notas de 2 recebidas seriam {nota2}
A quantidade de notas de 1 recebidas seriam {nota1}
'''
print(texto)