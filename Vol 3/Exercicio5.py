n1 = int(input('Insira um número inteiro positivo'))
n2 = int(input('Insira outro número inteiro positivo'))



while n1 % n2!= 0:
    n1, n2 = n2, n1 % n2
print(f'mdc = {n2}')