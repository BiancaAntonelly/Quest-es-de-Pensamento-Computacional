lista = []
for i in range(10):
  lista.append(int(input()))
lista.sort()
print(" ".join(map(str,lista)))