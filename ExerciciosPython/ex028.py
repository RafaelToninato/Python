import random
nr = random.randint(0, 6)
n = int(input('Digite um número inteiro de 0 a 5: '))
if n == nr:
    print('Você Acertou!')
else:
    print('Você Errou! O numero era {}'.format(nr))