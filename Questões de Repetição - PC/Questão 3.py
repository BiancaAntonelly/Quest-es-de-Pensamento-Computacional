número = int(input())
sum_divisores = 0
for i in range(número):
  if i != 0:
    if (número % i) == 0:
      sum_divisores += i
if sum_divisores == número:
  print('número perfeito')
else:
  print('número não é perfeito')