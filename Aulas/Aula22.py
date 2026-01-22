x = '0123456789'

print(x[0:2])
print(x[1:2])
print(x[2:4])
print(x[0:5])
print(x[1:8])

#pode se omitir o indice, sendo a omissão substituida pelo extremo correspondente
#a utilização de -1 e -2 tambem e valida sendo eles correspondentes ao ultimo e penultimos por sua vez

print(f'aqui {x[:2]}')
print(x[4:])
print(x[4:-1])
print(x[-4:-1])
print(x[:])

#Da pra se usar um incremento ao fatiar a string

texto = 'batatinha quando nasce'

texto[::2]
texto[::-1]