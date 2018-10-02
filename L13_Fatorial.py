#--------------------------------------------------------------------------------------------------
#Escreva um programa que receba um número natural n na entrada e imprima n! (fatorial) na saída.

#PASSOS:

# 1. Receber um número natural do usuário
# 2. Verificar se o número é natural
# 3. Calcular seu fatorial
# 4. Exibir o resultado
#--------------------------------------------------------------------------------------------------

numeronatural = int (input ("Digite o valor de n: "))

multiplicação = numeronatural - 1

fatorial = 1 

while multiplicação > 0:
    fatorial = numeronatural * multiplicação
    multiplicação = multiplicação - 1
    numeronatural = fatorial
print (fatorial)



