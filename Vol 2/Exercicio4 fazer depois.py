n1 = int(input("valor do primeiro número"))
n2 = int(input("valor do segundo número"))
n3 = int(input("valor do terceiro número"))

if n1 >= n2 and n1 >= n3:
    print("O primeiro número é maior")
elif n2 >= n3:
    print("O segundo número é maior")
else:
    print("O Terceiro Número é maior")
