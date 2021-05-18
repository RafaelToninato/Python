sal = float(input('Digite o salario: '))
if sal > 1250:
    print('O seu salario é de R${:.2f} e seu aumento foi de 10% por tanto seu '
          'salario atual é de R${:.2f}'.format(sal, sal + (sal * 0.10)))
else:
    print('O seu salario é de R${:.2f} e seu aumento foi de 15% por tanto seu '
          'salario atual é de R${:.2f}'.format(sal, sal + (sal * 0.15)))