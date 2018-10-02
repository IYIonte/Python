# Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função.

# NÚMEROS PRIMOS SÃO OS NÚMEROS QUE TEM APENAS 2 DIVISORES: O 1 E ELE MESMO

   
def maior_primo (x):
    n = x - 1
    o_numero_não_é_primo = False
    while n > 1 and x > 1:
        conta = x % n
        n = n - 1
        if conta == 0:
            o_numero_não_é_primo = True
            x = x - 1
            n = x - 1
    return (x)

            
    


