from random import randint

def SobreNome(vText, vNumber):
    print(f'O nome dele é : {vText}')

    if vNumber >= 10:
        print('Maior que 10!!')
    else:
        print('NADA!!')

vList = ['Matheus', 'Gabriel', 'Benjamim']

for vRange in vList:
    SobreNome(vRange, randint(1,12))
