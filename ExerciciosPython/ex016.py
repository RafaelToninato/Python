import math
print('Esse programa pega um número real e mostra sua porção inteira na tela')
n1 = float(input('Digite um número: '))
print('A porção inteira de {} é {}'.format(n1, math.trunc(n1)))