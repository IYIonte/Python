#---------------------------------------------------------------------------------------------------------
#Receber como entrada três valores: a, b e c

#Criar condições para a: a!=0 

#Usar fórmula de Bhaskara: Delta = b**2 - 4*a*c

#Criar condições para o valor de Delta, substituir valores na fórmula de Bhaskara e imprimir resultados:
#If Delta < 0:
#   print ("Não há raízes")
#If Delta = 0:
#   x = (-b + (math.sqrt(delta) /  2*a
#   print ("A raíz é igual a:", x)
#If Delta > 0:
#   x1 = (-b - (math.sqrt(delta) /  2*a
#   x2 = (-b + (math.sqrt(delta) /  2*a
#   print ("A raízes são:", x1,",", x2".")

#Resumo:
#Se delta é menor que zero = sem raízes reais
#Se delta é igual a zero = uma raíz real total
#Se delta é maior que zero = duas raízes reais

#Equação do 2º Grau: ax**2 + bx + c = 0
# x = variável
# a, b e c = constantes - a!=0

#Fórmula de Bhaskara: x = (-b +/- (math.sqrt(delta) /  2a
#--------------------------------------------------------------------------------------------------------

import math

a = float(input ("Insira o valor de 'a': "))
b = float(input ("Insira o valor de 'b': "))
c = float(input ("Insira o valor de 'c': "))

if a!=0:
    delta = (b**2) - (4*a*c)   
    if delta < 0:
        print ("esta equação não possui raízes reais")
    if delta == 0:
        y = math.sqrt(delta)
        x = (-b + y) / (2*a)
        print ("a raiz desta equação é", x)
    if delta > 0:
        y = math.sqrt(delta)
        x1 = (-b + y) / (2*a)
        x2 = (-b - y) / (2*a)
        if x1 <= x2:
            print ("as raízes da equação são", x1,"e", x2,".")
        else:
            print ("as raízes da equação são", x2,"e", x1,".")
             
else:
    print ("Por favor, insira um valor diferente de zero para 'a'!")
    a = int(input ("Insira o valor de 'a': "))
    delta = (b**2) - (4*a*c)   
    if delta < 0:
        print ("esta equação não possui raízes reais")
    if delta == 0:
        y = math.sqrt(delta)
        x = (-b + y) / (2*a)
        print ("a raiz desta equação é", x)
    if delta > 0:
        y = math.sqrt(delta)
        x1 = (-b + y) / (2*a)
        x2 = (-b - y) / (2*a)
        if x1 <= x2:
            print ("as raízes da equação são", x1,"e", x2,".")
        else:
            print ("as raízes da equação são", x2,"e", x1,".")
             

    
