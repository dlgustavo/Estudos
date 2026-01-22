José = 'Entrou as 6h'
def fatec():
    José = 'Entrou 8h'
    print(José)

print(José)
fatec()
print(José)


print('Utilizando global seguido de uma função ele vai pegar a função global(função que está fora do escopo da definição, caso contrario ele ira retornar a definição local)')
José = 'Entrou as 6h'
def fatec():
    global José
    José = 'Entrou 8h'
    print(José)

print(José)
fatec()
print(José)