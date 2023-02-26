somaidade = 0
mediadade = 0
maioridadeh = 0
nomevelho =''
totmulher20 = 0
for p in range(1,5):
    print('----- {} PESSOA -----'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade= somaidade + idade
    if p == 1 and sexo in 'Mm':
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediadade = somaidade / 4
print('A media de idade do grupo e de {:.1f} anos.'.format(mediadade))
print('O Homem mais velho tem {} anos e se chama {}.'.format(maioridadeh, nomevelho))
print('Sao {} mulhere(s) com menos de 20 anos.'.format(totmulher20))
