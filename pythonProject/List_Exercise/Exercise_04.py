# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
# população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários para que a
# população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

vHabitantesA = int(80000)
vHabitantesB = int(200000)
vAno = int(0)

while vHabitantesB > vHabitantesA:
    vHabitantesA += vHabitantesA * 0.03
    vHabitantesB += vHabitantesB * 0.015
    vAno += 1

print('Quantidade de anos: ', str(vAno))