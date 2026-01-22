tempo_de_ligação = int(input("Qual foi o tempo de ligação? "))

if tempo_de_ligação < 200:
    print("O valor da ligação é de: R$", tempo_de_ligação*0.20)
elif tempo_de_ligação >= 200 and tempo_de_ligação <= 400:
    print("O valor da ligação é de: R$", tempo_de_ligação*0.18)
elif tempo_de_ligação > 400 and tempo_de_ligação <= 800:
    print("O valor da ligação é de: R$", tempo_de_ligação*0.15)
elif tempo_de_ligação >= 800:
    print("O valor da ligação é de: R$", tempo_de_ligação*0.08)
