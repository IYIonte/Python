L = int (input ("Digite a largura do retângulo: ")) #largura
A = int (input ("Digite a altura do retângulo: ")) #altura
L1 = L
A1 = A

while A1 > 0:
    if A1 == 1 or A1 == A:
        while L1 > 0:
            print ("#", end = "")
            L1 = L1 - 1
        L1 = L
        A1 = A1 - 1

    elif A1 > 1 and A1 < A:
        while L1 > 0:
            if L1 == 1:
                print ("#", end = "")
                L1 = L1 - 1
            elif L1 > 1 and L1 < L:
                print (" ", end = "")
                L1 = L1 - 1
            elif L1 == L:
                print ("#", end = "")
                L1 = L1 - 1
        A1 = A1 - 1
        L1 = L
        
    print ()
    

