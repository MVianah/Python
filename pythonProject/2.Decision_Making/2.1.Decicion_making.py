vName = input('Nome do paciente: ')
vIdade = int(input('Idade do paciente: '))
vDoenca = input('O paciente possui alguma doença infecto-contagiosa: ').upper()

#PRIMEIRO PROBLEMA A SER RESOLVIDO
while vDoenca != 'SIM' and vDoenca != 'NAO':
    print('Digite SIM ou NAO')
    vDoenca = input('O paciente possui alguma doença infecto-contagiosa: ').upper()

if vDoenca == 'SIM':
    print('Encaminhe o paciente para a sala AMARELA')
else:
    print('Encaminhe o paciente para a sala BRANCA')


#SEGUNDO PROBLEMA A SER RESOLVIDO
if vIdade >= 65:
    print('Paciente COM prioridade')
else:
    vGenero = input('Qual o genero do paciente: ').upper()
    if vGenero == 'FEMININO' and vIdade > 10:
        vGravidez = input('A paciente está gravida: ').upper()
        if vGravidez == 'SIM':
            print('Paciente COM prioridade')
        else:
            print('Paciente SEM prioridade')
    else:
        print('Paciente SEM prioridade')

