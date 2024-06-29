class Bola:

    def __init__(self, Cor, Circunferencia, Material):
        self.Cor = Cor
        self.Circunferencia = Circunferencia
        self.Material = Material

    def trocarCor(self):
        self.Cor = input('Inserir Uma nova cor: ')
        self.mostrarCor()

    def mostrarCor(self):
        print(f'Cor : {self.Cor}')
        print(f'Circunferencia : {self.Circunferencia}')
        print(f'Material : {self.Material}')

    def msgTrocarCor(self):
        msg = input('Voce deseja trocar de cor?').upper()

        if msg == 'SIM':
            self.trocarCor()
        else:
           self.mostrarCor()

vDados = Bola('Azul', 3.45, 'Madeira')

vDados.msgTrocarCor()


