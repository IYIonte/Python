L = int (input ("Digite a largura do retângulo: ")) #largura
A = int (input ("Digite a altura do retângulo: ")) #altura
L1 = L

while A > 0:
    while L1 > 0:
        print ("#", end = "")
        L1 = L1 - 1
    A = A - 1
    L1 = L
    print ()
    
    
