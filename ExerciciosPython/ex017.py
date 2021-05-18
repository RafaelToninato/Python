import math
print('Esse programa calcula o comprimento da hipotenusa')
compop = float(input('Digite o comprimento do cateto oposto: '))
compad = float(input('Digite o comprimento do cateto adjacente: '))
print('O comprimento da hipotenusa é {:.2f}'.format(math.hypot(compop, compad)))