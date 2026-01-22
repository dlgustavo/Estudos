import random
rng = random.sample(range(100), 20)
par = []
impar = []

for numero in rng:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(f'lista de números gerados é {rng}')
print(f'lista de números pares gerados é {par}')
print(f'lista de números impares gerados é {impar}')