#Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista possui elementos repetidos e os remove.
#A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.
#Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?
#_____________________________________________________________________________________________________________________________________________________________________#
 
def remove_repetidos (lista):
    lista.sort ()
    quantidade = len (lista) - 1
    x = 0
    y = 1
    while y <= quantidade:
        if lista [(x)] == lista [(y)]:
            del lista [(y)]
            quantidade = quantidade - 1
        else:
            x = x + 1
            y = y + 1
    return lista 
