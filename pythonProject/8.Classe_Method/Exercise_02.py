class Squad:

    def __init__(self, Lado):
        self.Lado = Lado

    def trocarValor(self):
        self.Lado = int(input('Informe o novo valor: '))

    def retornaValor(self):

        print(f'O valor digitado e: {self.Lado}')

        msg = input('Deseja trocar o valor do lado do quadrado? ').upper()

        if msg == 'SIM':
            self.trocarValor()
            self.calcArea()
        else:
            self.calcArea()

    def calcArea(self):
        area = self.Lado**2
        print(f'A area do quadrado e: {area}')

vDados = Squad(2)

vDados.retornaValor()

