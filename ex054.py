maiorpeso = 0
menorpeso = 0
for j in range (1,6):
    peso = float(input('Digite o peso da {} pessoa: '.format(j)))
    if j == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print('O menor peso entre essas pessoa e {:.1f}'.format(menorpeso))
print('O maior peso entre essas pessoa e {:.1f}'.format(maiorpeso))

