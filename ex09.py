n = int(input('Informe um valor inteiro menor que 13: '))
x = n - 1
while x >= 1:
    n = (n * x)
    x = x - 1
print('O fatorial é {}'.format(n))
