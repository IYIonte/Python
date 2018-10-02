#Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve

#'Fizz' se o número for divisível por 3 e não for divisível por 5;

#'Buzz' se o número for divisível por 5 e não for divisível por 3;

#'FizzBuzz' se o número for divisível por 3 e por 5;

#Caso a função não seja divisível 3 e também não seja divisível por 5, ela deve devolver o número recebido como parâmetro.
#---------------------------------------------------------------------------------------------------------------------------

def fizzbuzz(x):
    y = x % 3
    q = x % 5
    if y == 0 and q == 0:
        return ("FizzBuzz")
    elif y == 0 and q > 0:
        return ("Fizz")
    elif y > 0 and q == 0:
        return ("Buzz")
    else:
        return (x)









    

