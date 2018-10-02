# Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

numero = int (input ("Digite um número inteiro: "))

n = 2
x = 0
o_numero_é_primo = False

while n < numero:
    x = numero % n
    n = n + 1
    if x == 0:
        o_numero_é_primo = True

if o_numero_é_primo:
    print ("não primo")

else:
    print ("primo")
    
    
