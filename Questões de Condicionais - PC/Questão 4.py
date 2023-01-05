C = int(input())
C1 = int(input())
C2= int(input())

distancia = C1 - C
distancia2 = C - C2

if (C1>C>C2 and ((C1 - C) > (C - C2))) or ((C2>C>C1) and (C2 - C ) > (C - C1)): 
  print("A")
elif C1>C>C2 and ((C1 - C) < (C - C2)) or ((C2 > C > C1) and ( C2 - C) < (C - C1)):
  print("F")
else:
  print ("C")