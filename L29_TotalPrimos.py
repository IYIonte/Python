#Escreva a função n_primos que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve a quantidade de números primos que existem entre 2 e n
#(incluindo 2 e, se for o caso, n).

def n_primos (x):
    fator = 2
    quantidade = 1
    while x > 2:
        while fator <= x:
            divisao = x % fator
            if divisao == 0:
                x = x - 1
            else:
                fator = fator + 1
            if fator == x:
                quantidade = quantidade + 1
                x = x - 1
        fator = 2
    return quantidade

