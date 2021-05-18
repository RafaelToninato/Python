velo = int(input('Digite a velocidade: '))
print('Você passou por um radar de 80Km\h á {}Km\h'.format(velo))
if velo >= 81:
    print('Você foi multado em R${:.2f}'.format((velo - 80) * 7))
