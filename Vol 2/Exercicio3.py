kg_limite = 50 #KG dia
kg_dia = float(input("Quantos KG de peixe no dia de hoje? "))
multa = (kg_dia - kg_limite) * 4.0


if kg_dia > kg_limite:
    print("Você excedeu o peso limite estabelecido a multa é de R$ ", multa)
else:
    print("Você está dentro do limite diario, não sera cobrado multa")