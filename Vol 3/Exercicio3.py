pop_a = 80000
pop_b = 200000
ycount = 0

while pop_a <= pop_b:
    pop_a = pop_a*1.03
    pop_b = pop_b*1.015
    ycount = ycount + 1
else:
    print(f'Em {ycount:.0f} anos a população do pais A ultrapassara a mesma população da População do pais B, tendo um total de {pop_a:.0f} habitantes e o Pais B {pop_b:.0f}')