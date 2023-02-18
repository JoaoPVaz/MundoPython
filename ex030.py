viagem = float(input('Digite a distancia da sua viagem: '))
if viagem <=200:
    preco = viagem * 0.50
else:
    preco = viagem * 0.45
print('O preco de sua passagem sera de R${:.2f}'.format(preco))