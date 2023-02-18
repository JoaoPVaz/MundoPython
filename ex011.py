produto = float(input('Digite o valor do produto: R$ '))
valordesc = float(input('Digite a porcentagem de desconto: '))
desc = produto * valordesc / 100
print('O novo valor do seu produto e R$ {:.2f}.'.format(produto - desc))