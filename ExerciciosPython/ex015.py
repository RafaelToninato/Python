print('Este programa calcula quanto um cliente deve pagar por um carro alugado')
d = int(input('Digite quantos Km foram rodados: '))
t = int(input('Digite quantos dias o carro foi alugado: '))
print('O carro foi alugado por {} dias e foram rodados {}Km! '
      '\nO total a ser pago é de R${:.2f}'.format(t, d, (60 * t) + (0.15 * d)))
