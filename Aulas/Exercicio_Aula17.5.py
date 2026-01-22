soma = 0
n = 0
while True:
    x = int(input("Informe o número (para finalizar digite 0): "))
    if x == 0:
        break
    else:
        n = n + 1
    soma = soma + x
print(f"Média dos números informados é: {soma/n:.1f}")