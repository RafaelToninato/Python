a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite outro número: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor digitado foi {}'.format(menor))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('o maior valor digitado foi {}'.format(maior))