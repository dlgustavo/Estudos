cigarros = int(input ("Quantos cigarros são fumados por dia?"))
anos_fumando = int(input ("Fuma a quanto tempo?'(em anos)"))
total_cigarros = cigarros * 365
tempo_perdido = total_cigarros * 10

print ("Levando em consideração que cada cigarro que você fuma é perdido 10 minutos de vida, neste periodo de", anos_fumando, ("Anos, foram perdidos"), tempo_perdido*conversao_dia, ("Dias"))
