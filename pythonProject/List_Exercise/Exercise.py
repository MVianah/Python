#Faça um programa que receba dois números e mostre qual deles é o maior.

vNum1 = int(input('Digite o primeiro numero: '))
vNum2 = int(input('Digite o segundo numero: '))

if vNum1 > vNum2:
    print('O primeiro numero e o MAIOR: ' + str(vNum1))
elif vNum2 > vNum1:
    print('O segundo numero e o MAIOR: ' + str(vNum2))
else:
    print('Os numeros são iguais')

