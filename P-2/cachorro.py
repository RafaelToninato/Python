class Cachorros:
    def __init__(self, nome, cor, idade, tamanho):
        self.nome = nome
        self.cor = cor
        self.idade = idade
        self.tamanho = tamanho

    def latir(self):
        print('au au')

    def correr(self):
        print('{} esta correndo'.format(self.nome))


cachorro_1 = Cachorros('Rex', 'caramelo', 3, 'pequeno')
cachorro_2 = Cachorros('Fox', 'preto', 5, 'grande')

cachorro_2.correr()
