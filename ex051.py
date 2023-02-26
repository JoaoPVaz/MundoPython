numero = int(input('Digite um numero: '))
tot = 0
for i in range (1, numero + 1):
    if numero % i == 0:
        print('\033[33m', end=' ')#Numeros divisiveis
        tot = tot + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(i), end='')
print('\n\033[m O numero {} foi dividido {} vezes.'.format(numero, tot))
if tot == 2:
    print('Este numero e PRIMO ! ')
else:
    print('Este numero NAO E PRIMO ! ')
