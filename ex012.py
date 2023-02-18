salario = float(input('Qual e o salario do Funcionario ? R$ '))
ajuste = float(input('Qual a porcentagem de reajuste ? '))
novo = salario * ajuste /100
print('O Funcionario que recebia R$ {:.2f}, passara a receber R${:.2f}, apos o reajuste de {:.0f}%'.format(salario, novo + salario, ajuste))
