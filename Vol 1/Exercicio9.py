dias = int(input ("Por quantos dias o carro foi alugado? "))
kms = float(input ("Quantos Kms foram rodados? "))
diavalor = dias*60
kmsvalor = kms*0.15
print("De acordo com os dados informados, será gasto o total de R$", diavalor + kmsvalor)