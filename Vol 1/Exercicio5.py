ogval = float (input ("Qual valor da mercadoria?"))
desconto = float (input ("Quanto de desconto?(utilize apenas o número)"))
descontoval = desconto/100*ogval
print ("o valor de desconto recebido é de: R$", descontoval)
print ("O valor final do produto é de: R$", ogval - descontoval)