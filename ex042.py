peso = float(input('Digite seu peso: (Kg) '))
alt = float(input('Digite sua altura: (m) '))
imc = peso / (alt ** 2)
print('O IMC desta pessoa e igual a {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta ABAIXO DO PESO NORMAL')
elif imc >= 18.5 and imc < 25:
    print('PARABENS, Voce esta no PESO IDEAL')
elif imc >=  20 and imc < 30:
    print('Voce esta SOBREPESO')
elif imc >= 30 and imc < 40:
    print('CUIDADO ! Voce esta com OBESIDADE')
else:
    print('PROCURE UM MEDICO !! ', end='')
    print('Voce esta em OBESIDADE MORBIDA')

