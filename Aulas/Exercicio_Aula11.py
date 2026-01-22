velocidade_via = 110
velocidade_carro = int(input("Qual a velocidade que você estava? "))
valor_multa = 5
if velocidade_carro > velocidade_via:
    print("Parabéns animal, você foi multado em R$", (velocidade_carro-velocidade_via)*valor_multa)
else:
    print("Desculpa o incomodo ae meu patrão pode seguir viagem")