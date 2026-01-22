print('for tem a mesma função que while, porem sem a nescecidade de usar contadores')

for letra in 'aeiou':
    print(letra)


print('exemplo utilizando while')
texto = 'aeiou'
k = 0
while k < len(texto):
    letra = texto[k]
    print(letra)
    k= k + 1


print('utilizando for')
for i in range(5):
    print(i)

print('utilizando while')
lista = list(range(5))
k = 0

while k < len(lista):
    i = lista[k]
    print(i)
    k = k + 1