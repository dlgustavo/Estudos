n_informado = int(input('Informe o número a ser calculado Fibonacci'))
na = 1
nb = 1

while na + nb <= n_informado:
    print(f'{na} + {nb} = {na + nb}')
    proximo = na + nb
    na = nb
    nb = proximo
    