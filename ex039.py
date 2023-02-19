n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('A MEDIA de {:.2f} e {:.2f} equivale a {:.2f} pontos.'.format(n1, n2, media))
if media >= 7:
    print(('Aluno APROVADO !'))
elif media > 6.9 or media > 5 :
    print('O Aluno esta em RECUPERACAO')
else:
    print('Aluno REPROVADO')
