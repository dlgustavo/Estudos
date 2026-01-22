nf = int(input("Informe o número a ser fatorado"))

k = 1
fat = 1

while k <= nf:
    fat = fat * k
    k = k + 1
print (f"fat({nf}) = {fat}")