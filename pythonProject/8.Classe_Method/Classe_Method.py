class Pessoa:

    def __init__(self, Name, Idade):
        self.Name = Name
        self.Idade = Idade

    def boasVindas(self):
        print(f'Login realizado com sucesso, Parabens!!! Usuario: {self.Name}')

    def recusado(self):
        print(f'Login não realizado, Usuario: {self.Name}')

    def Maior_Idade(self):
        if self.Idade >= 18:
            print(f'Usuario Maior de idade {self.Idade}')
            self.boasVindas()
        else:
            print(f'Usuario Menor de idade {self.Idade}')
            self.recusado()

vName = input('Informe seu Nome: ')
vIdade = int(input('Informe sua Idade: '))

Dados = Pessoa(vName, vIdade)

Dados.Maior_Idade()
