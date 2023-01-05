import math
Nadadores = 0
tempo = float(input())
for i in range(100):
    Valor = float(input())
    if Valor == (-1):
        break
    elif Valor <= tempo:
        Nadadores += 1
Series = (Nadadores / 8)
print (Nadadores)
print (math.ceil(Series))