from math import pow
n = int(input('Informe um numero inteiro menor que 1000: '))
cont = 1
while cont <= n:
    print('{} {} {}'.format(cont, int(pow(cont, 2)), int(pow(cont, 3))))
    cont = cont + 1
