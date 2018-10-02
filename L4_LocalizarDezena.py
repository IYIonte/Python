#------------------------------
#Etapas:

#inserir um número inteiro;
#localizar o digito da dezena;
#mostrar o digito.
#------------------------------

numero = input ("Digite um número inteiro: ")

x = len(numero)

if x < 2:
	print("O dígito das dezenas é 0")

if x > 2:
    y = x - 2
    selecionado = numero [y]
    print("O dígito das dezenas é", selecionado)

if x == 2:
    y = x - 2
    selecionado = numero [y]
    print("O dígito das dezenas é", selecionado)





