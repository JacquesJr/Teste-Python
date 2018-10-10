lista = input('Digite dois valores(separados por espaço): ').split(' ')
A = int(lista[0])
B = int(lista[1])
valor = B / A
if valor // 1 == valor:
    print('São Multiplos')
else:
    print('Não são Multiplos')
