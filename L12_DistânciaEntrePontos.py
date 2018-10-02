import math

x1 =  int (input ("Digite um número inteiro: "))
y1 =  int (input ("Digite um número inteiro: "))

x2 =  int (input ("Digite um número inteiro: "))
y2 =  int (input ("Digite um número inteiro: "))

# A = (x1, y1)
# B = (x2, y2)

DISTÂNCIA = math.sqrt (((x2-x1)**2) + ((y2 - y1)**2))

if DISTÂNCIA >= 10:
    print ("longe")
else:
    print ("perto")
