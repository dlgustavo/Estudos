f = open(r'C:\Users\Gustavo\Downloads\xd.txt','w')

for linha in range(1, 101):
    f.write(f'{linha}\n')
f.close()


f = open(r'C:\Users\Gustavo\Downloads\xd.txt')

for linha in f.readlines():
    print(linha.strip())
f.close()

print('exemplo de como executar o codigo de leitura em 1 linha usando with')

with open (r'C:\Users\Gustavo\Downloads\xd.txt') as f:
    print(f.read())