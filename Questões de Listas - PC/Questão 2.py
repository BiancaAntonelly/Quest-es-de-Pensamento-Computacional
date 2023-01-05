alunos = []
notas = []
acima = []
for i in range(5):
  nome = str(input())
  alunos.append(nome)
  valor = int(input())
  notas.append(valor)

media = sum(notas) / 5
print("Média:", media)
for i in range(5):
  if notas[i] >= media:
    acima.append(alunos[i])
print ("Acima da média:", ",".join(map(str, acima)))
print ("Maior nota:", alunos[notas.index(max(notas))])
#print(alunos)
#print(notas)
