import random
print('Este programa irá sortear entre 4 alunos, 1 para apagar o quadro negro')
al1 = input('Escreva o nome de um dos alunos: ')
al2 = input('Escreva o nome de outro aluno: ')
al3 = input('Escreva o nome de outro aluno: ')
al4 = input('Escreva o nome de outro aluno: ')
vars = [al1, al2, al3, al4]
print('O aluno sorteado foi {}'.format(random.sample(vars, 1)))
