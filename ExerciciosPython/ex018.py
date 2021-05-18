from math import radians, sin, cos, tan
print('Este programa calcula o seno, o cosseno e a tangente de um ângulo')
ang = float(input('Digite um ângulo: '))
print('O seno é {:.2f} \n O cosseno é {:.2f} \n A tangente é {:.2f}'
      .format(sin(radians(ang)), cos(radians(ang)), tan(radians(ang))))