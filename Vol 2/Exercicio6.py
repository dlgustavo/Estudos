salario_hora = float(input("Quanto você recebe por hora? "))
horas_trabalhadas = float(input("Quantas horas trabalhadas mensalmente? "))
salario_bruto = salario_hora * horas_trabalhadas
desconto_inss = (salario_bruto * 0.11) 
desconto_ir = (salario_bruto * 0.08)
desconto_sindicato = (salario_bruto * 0.05)
salario_liquido = salario_bruto - desconto_inss - desconto_sindicato - desconto_ir

texto = f'''
O valor original que você receberia seria de R${salario_bruto}
Apos os descontos você recebera R${salario_liquido}
Você esta sendo descontado um valor de R${desconto_inss} referente ao INSS
R${desconto_ir} referente ao imposto de renda
R${desconto_sindicato} referente ao desconto do sindicato
'''
valor = print(texto)
