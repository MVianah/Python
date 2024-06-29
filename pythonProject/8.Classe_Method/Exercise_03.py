print('****************** RETANGULO *******************')
vBase = float(input('Informe o valor da base do ratangulo: '))
vAltura = float(input('Informe o valor da altura do retangulo: '))
print('*************** AREA ***************')
vLado1 = float(input('Informe a primeira medida: '))
vLado2 = float(input('Informe a segunda medida: '))


class Rectangle:

    def __init__(self, Base, Altura):
        self.Base = Base
        self.Altura = Altura

    def mudarValor(self):
        print('\n')
        print('*************** ALTERAÇÃO ***************')
        msg = input('Deseja realizar alguma alteração nos valores do Retângulo? ').upper()

        if msg == 'SIM':
            self.Comprimento = float(input('Informe o novo valor da Base: '))
            self.Altura = float(input('Informe o novo valor da Altura: '))

    def retornarValor(self):
        self.mudarValor()
        self.calcArea()

    def calcArea(self):
        vArea = self.Altura * self.Base
        print('\n')
        print('*************** RESULTADO ***************')
        print(f'O Valor da area e do piso:  {vArea}')

class Area:
    def __init__(self, Comprimento, Altura):
        self.Comprimento = Comprimento
        self.Altura = Altura

    def mudarValor(self):
        print('\n')
        print('*************** ALTERAÇÃO ***************')
        msg = input('Deseja realizar alguma alteração nos valores da Area? ').upper()

        if msg == 'SIM':
            self.Comprimento = float(input('Informe o novo valor do Comprimento: '))
            self.Altura = float(input('Informe o novo valor da Altura: '))

    def retornarValor(self):
        self.mudarValor()
        self.calcArea()

    def calcArea(self):
        vArea = self.Altura * self.Comprimento
        print('\n')
        print('*************** RESULTADO ***************')
        print(f'O Valor da area e {vArea}')

vPiso = Rectangle(vBase, vAltura)
vPiso.retornarValor()

vArea = Area(vLado1,vLado2)
vArea.retornarValor()

