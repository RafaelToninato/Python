import random

print('Este programa fará a seleção de qual aluno irá apresentar seu trabalho em primeiro')
al1 = input('Digite o nome do primeiro aluno: ')
al2 = input('Digite o nome do segundo aluno: ')
al3 = input('Digite o nome do terceiro aluno: ')
al4 = input('Digite o nome do quarto aluno: ')
vars = (al1, al2, al3, al4)
print('Os trabalhos serão apresentados nesta ordem \n{}'.format(random.sample(vars, 4)))