#programa que recebe uma sequência de números dados pelo usuário, e calcule o fatorial de cada número.

#dica: while mais externo para receber os números e um while mais interno para calcular o fatorial. 

x = 0

while x >= 0:
    x = int (input ("Digite o valor de n: "))
    multiplicação = x - 1
    fatorial = 1
    while multiplicação > 0:
        fatorial = x * multiplicação
        multiplicação = multiplicação - 1
        x = fatorial
    print (fatorial)
        
