check = int(input('Insira um número para verificar se é triangular'))
n1 = 1
n2 = 2
n3 = 3

while n1 * n2 * n3 < check:
    n1, n2, n3 = n2, n3, n3 + 1

if n1 * n2 * n3 == check:
    print(f'{check} é triangular')

else:
    print(f'{check} não é triangular')