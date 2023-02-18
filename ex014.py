dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos KM foi percorrido ? '))
valor = (dias * 60) + (km * 0.15)
print('O valor do aluguel corresponde aos {} dias, e igual a R${:.2f}'.format(dias, valor))