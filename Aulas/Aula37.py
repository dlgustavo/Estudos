f = open(r'C:\Users\Gustavo\Desktop\Eu sabo\Python\PPZ-master\surf.txt')
maior = 0
for linha in f:
    nome, pontos = linha.split()
    if float(pontos) > maior:
        maior = float(pontos)
f.close
print(maior)



print('Codigo que pegue as notas, coloca em lista e arranja do maior para menor para descobrir as 3 maiores notas')

f = open(r'C:\Users\Gustavo\Desktop\Eu sabo\Python\PPZ-master\surf.txt')
notas = []

for linha in f:
    nome, pontos = linha.split()
    notas.append(float(pontos))
f.close()
notas.sort()
notas.reverse()
print (notas[0])
print (notas[1])
print (notas[2])

print('O mesmo codigo a cima porem incluindo o nome de quem tirou a nota')

f = open(r'C:\Users\Gustavo\Desktop\Eu sabo\Python\PPZ-master\surf.txt')
notas = {}

for linha in f:
    nome, pontos = linha.split()
    notas[float(pontos)] = nome
f.close()
for nota in sorted (notas, reverse = True):
    print (f'{notas[nota]} tem nota {nota}')
