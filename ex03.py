from math import pow
from math import sqrt
ponto1 = input("Informe os valores do primeiro ponto(separados por espaço): ").split(' ')
x1 = float(ponto1[0])
y1 = float(ponto1[1])
ponto2 = input("Informe os valores do segundo ponto(separados por espaço): ").split(' ')
x2 = float(ponto2[0])
y2 = float(ponto2[1])
distancia = sqrt((pow(x2 - x1, 2)) + (pow(y2 - y1, 2)))
print('A distância é igual a {:.4f}'.format(distancia))
