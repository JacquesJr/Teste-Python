numero = int(input("Informe o número do funcionário: "))
horas = int(input("Informe o número de horas trabalhadas pelo funcionário: "))
valor = float(input("Informe o valor que o funcionário recebe por hora: "))
valortotal = float(valor * horas)
print('NUMBER = {}\nSALARY = U$ {:.2f}'.format(numero, valortotal))
