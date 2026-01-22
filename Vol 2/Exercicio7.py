area_coberta = float(input("Quantos metros precisam ser cobertos? "))
metros_lata = 54
latas_nesc = area_coberta / metros_lata
valor_total_ared = int(latas_nesc+1)

if area_coberta % 54 != 0:
    print("Você precisara comprar", valor_total_ared, "Latas de tinta, totalizando um valor de R$", valor_total_ared*80)
else:
    print("Você precisara comprar", round(latas_nesc), "Latas de tinta, totalizando um valor de R$", latas_nesc*80)