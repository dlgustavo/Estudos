texto = open(r'C:\Users\Gustavo\Desktop\Eu sabo\Python\PPZ-master\mensagem.txt', 'r')
cript = open(r'C:\Users\Gustavo\Downloads\Cripto.txt', 'w')

for linha in texto.readlines():
    for letra in linha:
        if letra in 'aeiouãõ':
            cript.write('*')
        else:
            cript.write(letra)

texto.close()
cript.close()


def ip_ok(ip):
    ip = ip.split('.')
    for byte in ip:
        if int(byte) > 255:
            return False
    return True


arq = open(r'C:\Users\Gustavo\Desktop\Eu sabo\Python\PPZ-master\IPS.txt')
validos = open(r'C:\Users\Gustavo\Downloads\Validos.txt', 'w')
invalidos = open(r'C:\Users\Gustavo\Downloads\Invalidos.txt', 'w')

for linha in arq.readlines():
    if ip_ok(linha):
        validos.write(linha)
    else:
        invalidos.write(linha)

arq.close()
validos.close
invalidos.close