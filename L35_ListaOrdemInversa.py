#Como pedido na primeira video-aula desta semana, escreva um programa que recebe uma sequência de números inteiros terminados por 0 e imprima todos os valores
#em ordem inversa. Note que 0 (ZERO) não deve fazer parte da sequência.

lista = []
elemento = 1

while elemento != 0:
    elemento = int (input ("Digite a sequencia de números desejas e interrompa com o número 0: "))
    if elemento != 0:
        lista.append (elemento)
    else:
        quantidade = len (lista) - 1
        while quantidade >= 0:
            print (lista [quantidade])
            quantidade = quantidade - 1

