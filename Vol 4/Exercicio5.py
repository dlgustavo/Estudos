texto ="The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you"
texto = texto.replace(',','')
texto = texto.replace('.','')
texto = texto.replace(':','')
textodiv = texto.split(' ')
batata = []

for palavra in textodiv:
    if palavra.lower()[0] == 'p' or palavra.lower()[-1] == 'p':
        batata.append(palavra)

    elif palavra.lower()[0] == 'y' or palavra.lower()[-1] == 'y':
        batata.append(palavra)

    elif palavra.lower()[0] == 't' or palavra.lower()[-1] == 't':
        batata.append(palavra)

    elif palavra.lower()[0] == 'h' or palavra.lower()[-1] == 'h':
        batata.append(palavra)

    elif palavra.lower()[0] == 'o' or palavra.lower()[-1] == 'o':
        batata.append(palavra)

    elif palavra.lower()[0] == 'n' or palavra.lower()[-1] == 'n':
        batata.append(palavra)

print(f'as palavras que começam ou terminam com as letras p,y,t,h,o,n são {batata}')
tamanho_palavra = []

for palavra in batata:
    if len(palavra) > 4:
        tamanho_palavra.append(palavra)

print(f'tendo um total de {len(tamanho_palavra)} com 4 ou mais caracteres')


