#--------------------------------------------------------------------------------------------------------------------------------------------------
# Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.

# PASSOS:

# 1. Receber um número inteiro positivo do usuário
# 2. Verificar se o número é inteiro e positivo
# 3. Verificar os números impares
# 4. Exibir os n primeiros números impares

# 1 2 3 4 5 6 7 8 9 10   11 12 13 14 15 16 17 18 19 20 
#--------------------------------------------------------------------------------------------------

numero = float (input ("Digite o valor de n: "))

x = 1

while x <= (numero * 2) - 1:
    y = x % 2
    if y > 0:
        print (x)
    x = x + 1


    
        
            
