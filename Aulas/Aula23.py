s = 'um tigre, dois tigres, três tigres'
s.find('tigre', 4)
print('Aqui ele vai procurar onde está a palavra tigre atraves do index a partir da posição informada(4)')
print(f'{s.find('tigre', 4)}')

s.replace('tigre', 'gato')
print('Aquie esta sendo utilizado a funcionalidade replace que ira subistituir na string s tigre por gato')
print(f'{s.replace('tigre', 'gato')}')

s = s.replace('tigre', 'gato')
print('Devido ao fato de que strings são imutaveis caso eu queira fazer uma substituição permanente na string é utilizado string = string.replace')
print(s)