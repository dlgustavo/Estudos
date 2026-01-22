palavra = input('Informe uma palavra para ser verificado se é palindrome a')
palavra_invertida = palavra[::-1]

if palavra != palavra_invertida:
    print(f'{palavra} não é palindrome')
else:
    print(f'A palavra {palavra} é palindrome')