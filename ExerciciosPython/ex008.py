print('Este programa é um conversor de medidas.')
m = float(input('Digite um número: '))
print('de {}m para \n{:.0f}cm \n{:.0f}mm \n{:.0f}dm \n{:.1f}dam \n{:.2f}hm \n{:.3f}km'.format(m, m * 100, m * 1000, m * 10, m * 0.1, m * 0.01, m * 0.001))
