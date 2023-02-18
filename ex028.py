velocidade = float(input('Qual e a velocidade atual do carro ? '))
if velocidade > 80:
    print('MULTADO! Voce excedeu o limite da Via que e de 80 Km/h. ')
    multa = (velocidade - 80) *7
    print('Voce deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um Bom dia ! Dirija com seguranca!')