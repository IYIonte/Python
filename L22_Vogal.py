#Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.

def vogal (n1):
    vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    if n1 in vogais:
        n1 = True
    else:
        n1 = False
    return n1
        
    
