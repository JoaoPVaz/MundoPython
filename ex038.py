from datetime import date
atual = date.today().year
anonasc = int(input('Ano de Nascimento: '))
idade = atual - anonasc
print('Quem nasceu em {} tem {} anos em {}'.format(anonasc, idade, atual))
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Voce ainda nao tem 18 anos. Ainda faltam {} ano(s) para o seu alistamento.'.format(saldo ))
    ano = atual + saldo
    print('Seu alistamento sera em {}.'.format(ano))
else:
    saldo = idade - 18
    print('Voce ja deveria ter se alistado ha {} ano(s)'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento deveria ter sido em {}.'.format(ano))
