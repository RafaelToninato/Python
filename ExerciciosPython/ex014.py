print('Este programa converte a temperatura de ºC para ºF')
tempc = float(input('Digite uma temperatura em ºC: '))
print('De {:.1f}ºC para {:.1f}ºF'.format(tempc, 32 + tempc * 1.8))