import math
valor = int(input())
juros = float(input()) / 100
quantiade_mes = int(input())
mes = 0
for _ in range(quantiade_mes):
  mes += 1
  print("mês:", str(mes))
  valor = math.floor(valor*100)/100
  print('saldo anterior: ' + str("%.2f" % valor))
  juros_mes = float(valor) * float(juros)
  juros_mes = math.floor(juros_mes*100)/100
  print('juros mês: ' + str("%.2f" % juros_mes))
  valor = float(valor) + float(juros_mes)
  valor = math.floor(valor*100)/100
  print('novo saldo: ' + str("%.2f" % valor))
  if mes != quantiade_mes:
    print("-")
  else:
    print('')