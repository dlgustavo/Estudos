usuario = input("digite seu usuario ")
senha = input("digite sua senha ")

while usuario == senha:
    print("Senha e usuario não podem ser os mesmo, tente novamente")
    senha = input("digite a sua senha")
else:
    print("Login efetuado com sucesso ")