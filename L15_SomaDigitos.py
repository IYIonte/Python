#--------------------------------------------------------------------------------------------------------------------------------
# Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída

# PASSOS:

# 1. Receber um número inteiro do usuário
# 2. Desmembrar os número 
# 3. Somar os números
# 4. Mostrar a soma
#--------------------------------------------------------------------------------------------------------------------------------

numero = int (input ("Digite um número inteiro: "))

quantidade_divisão = len (str(numero))

y = 0

while quantidade_divisão > 0:
    x1 = numero % 10
    numero = numero // 10
    quantidade_divisão = quantidade_divisão - 1
    y = y + x1

print (y)





