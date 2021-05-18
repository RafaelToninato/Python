dist = int(input('Digite a distancia da viagem: '))
if dist <= 200:
    print('A distancia da viagem é de {}Km e ela custará R${:.2f}'.format(dist, dist * 0.5))
else:
    print('A distancia da viagem é de  {}Km e ela custará R${:.2f}'.format(dist, dist * 0.45))