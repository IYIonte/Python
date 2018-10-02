#Reescreva a função 'maximo' do exercício 2, que devolve o maior valor dentre dois inteiros recebidos, para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.


def maximo (x, y, w):
    if x > y and x > w:
        return (x)
    elif y > x and y > w:
        return (y)
    elif w > x and w > y:
        return (w)
    elif x == y == w:
        return (x)

        
                    
