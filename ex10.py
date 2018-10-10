frase = str(input('Digite uma frase: '))
letra = str(input('Digite uma letra: '))
n = len(frase)
cont = 0
while n >= 0:
    if frase[n-1] == letra[0]:
        cont = cont + 1
    n = n - 1
print('A letra aparece {} vezes na frase'.format(cont))
