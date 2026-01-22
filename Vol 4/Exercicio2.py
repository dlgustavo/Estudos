import random
rng = []
par = []
impar = []

for numero in random.sample(range(100), 20):
    rng.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(f'lista de números gerados é {rng}')
print(f'lista de números pares gerados é {par}')
print(f'lista de números impares gerados é {impar}')