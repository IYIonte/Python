# Descobrir quais números entre 1 e n que são comprimentos de hipotenusas de algum triângulo retangulo com catetos inteiros

# cateto1² + cateto2² = hipotenusa²

# A HIPOTENUSA É O LADO MAIOR DO TRIÂNGULO, LOGO CATETOS SERÃO MENORES QUE A HIPOTENUSA

import math

def soma_hipotenusas (n):
    cateto1 = 1
    cateto2 = 1
    hip = 1
    HipQuad = hip ** 2
    SomaCatsQuad = (cateto1 ** 2) + (cateto2 ** 2)

    soma = []
    
    while hip <= n:
        while cateto1 < n:
            while cateto2 < n:
                if HipQuad == SomaCatsQuad:
                    #adicionar a lista
                    soma.append (n)
                else:
                    cateto2 = cateto2 + 1
                    SomaCatsQuad = (cateto1 ** 2) + (cateto2 ** 2)
            cateto2 = 1
            cateto1 = cateto1 + 1
            SomaCatsQuad = (cateto1 ** 2) + (cateto2 ** 2)
        hip = hip + 1
        HipQuad = hip ** 2
        cateto1 = 1
        cateto2 = 1
        SomaCatsQuad = (cateto1 ** 2) + (cateto2 ** 2)
        
    soman = list(set(soma))
    somatotal = sum (soman)
        
    return somatotal
    
