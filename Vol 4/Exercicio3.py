import random
lista1 = random.sample(range(100), 10)
lista2 = random.sample(range(100), 10)
lista3 = []

for numero in range(10):
    lista3.append(lista1[numero])
    lista3.append(lista2[numero])
lista3.sort()


print(lista1)
print(lista2)
print(lista3)

