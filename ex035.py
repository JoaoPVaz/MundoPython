vcasa = float(input('Qual o valor da casa ? R$ '))
fsalario = float(input('Qual o salario do comprado ? R$ '))
anos = float(input('Quantos anos pretende financiar ? '))
prestacao = vcasa / (anos * 12)
min = fsalario * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos.'.format(vcasa, anos), end ='')
print(' a prestacao sera de R$ {:.2f}'.format(prestacao))
if prestacao <= min:
    print('Emprestimo pre aprovado !')
else:
    print('Emprestimo NEGADO !', end = '')
    print(' Tente Novamente daqui 3 meses !')