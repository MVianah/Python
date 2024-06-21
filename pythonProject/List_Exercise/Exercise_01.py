#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
vNota = int(input('Digite um valor de 0 a 10: '))

while vNota < 0 or vNota > 10:
    print('Valor invalido informe um valor valido de 0 a 10')
    vNota = int(input('Digite um valor de 0 a 10: '))

if vNota >= 0 and vNota <= 10:
    print('Valor valido: ' + str(vNota))


