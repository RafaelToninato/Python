print('Este programa irá mostrar quantos dolares a quantia de reias digitada pode comprar')
r = float(input('Digite a quantia em reais: R$'))
print('Com R${:.2f} você pode comprar essa quantia em US${:.2f}'.format(r, r / 3.27))