from datetime import date
ano = int(input('Digite um ano ou digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Este ano é um ano bissexto por tanto ele contem 366 dias!')
else:
    print('Este ano não é um ano bissexto por tanto ele contem 365 dias!')