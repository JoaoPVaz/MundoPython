print('='*20)
print(' TERMOS DE UMA PA ')
print('='*20)
primeiro = int(input('Primeiro TERMO: '))
razao = int(input('RAZAO: '))
decimo = primeiro + (10-1) * razao
for i in range(primeiro, decimo , razao):
    print('{}'.format(i), end=' -> ')
print('ACABOU!')