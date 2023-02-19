print('-=' * 10, end='')
print(' LOJAS VAZ TECH ', end='')
print('-=' * 10)
valor = float(input('Preco das compras: R$ '))
print(''' FORMAS DE PAGAMENTOS
[ 1 ] a vista dinheiro / cheque
[ 2 ] a vista cartao
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao ''')
opcao = int(input('Digite a opcao desejada: '))
if opcao == 1:
    total = valor - (valor * 10 / 100)
    print('O valor de {} saira ao total com 10% de desconto a R$ {:.2f}'.format(valor, total))
elif opcao == 2:
    total = valor - (valor * 5 / 100)
    print('O valor de {} saira ao total com 5% de desconto a R$ {:.2f}'.format(valor, total))
elif opcao == 3:
    print('O valor total sera de R$ {:.2f}.'.format(valor))
elif opcao == 4:
    total = valor + (valor * 20 / 100)
    parc = int(input('Quantas parcelas deseja sua compra ?: '))
    totparc = total / parc
    print('Sua compra sera parcelada em {}x '.format(parc), end='')
    print('Cada parcela sera no valor de {} '.format(totparc))
else:
    print('OPCAO INVALIDA !!! TENTE NOVAMENTE')
