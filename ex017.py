import math
angulo = float(input('Digite o angulo que voce deseja: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print('O angulo digitado e {};'.format(angulo))
print('O seno deste angulo equivale a {:.2f}'.format(seno))
print('O cosseno deste angulo equivale a {:.2f}'.format(cos))
print('A tangente deste angulo equivale a {:.2f}'.format(tang))