ano = int(input("Qual o ano?"))



if ano % 4:
    print("Bisexto")
elif ano % 400 > 0:
    print("Bisexto")
else:
    print("Não é Bisexto")
