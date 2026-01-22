Lado1 = float(input("Comprimento do primeiro lado"))
Lado2 = float(input("Comprimento do segundo lado"))
Lado3 = float(input("Comprimento do terceiro lado"))

if Lado1 > Lado2 + Lado3 or Lado3 > Lado1 + Lado2 or Lado2 > Lado1 + Lado3:
    print("Não pode ser um triangulo")
elif Lado1 == Lado2 == Lado3:
    print("Essa merda é Equilatero")
elif Lado1 == Lado2 and Lado1 != Lado3 or Lado1 == Lado3 and Lado2 != Lado3:
    print("Essa merda é Isósceles")
elif Lado1 != Lado2 != Lado3:
    print("Ta tudo torto")
