# G. dista10
# seja um inteiro n
# retorna True se a diferença absoluta entre n e 100 ou n e 200
# for menor ou igual a 10
# dista10(93) -> True
# dista10(90) -> True
# dista10(89) -> False
def dista10(n):
  from math import abs
  if abs(n - 100) <= 10 or abs(n - 200) <= 200:
    return True
  return False