import math
'''catop = float(input('Digite o valor do cateto oposto: '))
catadj = float(input('Digite o valor do cateto adjacente: '))
hi = (catop ** 2 + catadj ** 2) ** (1/2)
print('O valor da hipotenusa sera de {:.2f}'.format(hi))'''

catop = float(input('Digite o valor do cateto oposto: '))
catadj = float(input('Digite o valor do cateto adjacente: '))
hi = math.hypot(catop, catadj)
print('O valor da hipotenusa sera de {:.2f}'.format(hi))