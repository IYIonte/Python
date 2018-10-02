#---------------------------------------------------------------------------------------------
#Dado um número, dizer se esse número tem números adjacentes (um do lado do outro) iguais

#Passos:

# Pedir para que o usuário digite o número
# Reconhecer se o número tem digitos adjacentes iguais
# Exibir 'sim' caso tenha e 'não' caso não tenha
#---------------------------------------------------------------------------------------------

numero = int (input("Insira um número inteiro: "))

quantidade_divisão = len (str(numero))

tem_numero_adjacente_igual = False

x1 = numero % 10
numero = numero // 10
quantidade_divisão = quantidade_divisão - 1

x2 = numero % 1
numero = numero // 10
quantidade_divisão = quantidade_divisão - 1

if x2 == x1:
    tem_numero_adjacente_igual = True

else:
    while quantidade_divisão > 0:
        x1 = numero % 10
        numero = numero // 10
        quantidade_divisão = quantidade_divisão - 1

        if x2 == x1:
            tem_numero_adjacente_igual = True

        else:
            x2 = numero % 10
            numero = numero // 10
            quantidade_divisão = quantidade_divisão - 1

            if x2 == x1:
                tem_numero_adjacente_igual = True
    
  
if tem_numero_adjacente_igual:
    print ("sim")
else:
    print ("não")

