num = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para conversao: ')
print(' [ 1 ] para converter em binario ')
print(' [ 2 ] para converter em octal ')
print(' [ 3 ] para converter em hexadecimal ')
opcao = int(input('Sua Opcao: '))
if opcao == 1:
    print('{} convertido para BINARIO e igual a {}.'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL e igual a {}.'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL e igual a {}.'.format(num, hex(num)[2:]))
else:
    print('Opcao Invalida, tente novamente !')