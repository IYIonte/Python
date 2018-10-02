#--------------------------------------------------------------------------------
#Mensagem a ser exibida:

#Olá, Fulano de Tal
#A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada.

#Processos:

#inserir o nome do cliente;
#inserir dia de vencimento;
#inserir mes de vencimento;
#inserir valor da fatura;
#exibir mensagem final.
#-------------------------------------------------------------------------------

nomedocliente = input ("Digite o nome do cliente: ")
diadovencimento = input ("Digite o dia de vencimento: ")
mesdovencimento = input ("Digite o mês de vencimento: ")
valordafatura = input ("Digite o valor da fatura: ")

print("Olá,", nomedocliente)
print("A sua fatura com vencimento em", diadovencimento, "de", mesdovencimento, "no valor de R$", valordafatura, "está fechada.")

      
