vName = input('Digite o nome do paciente: ')
vIdade = int(input('Digite a idade do paciente: '))
vDoenca = input('O paciente possui alguam doença infecto-Contagiosa? ').upper()

if vIdade >= 65:
    print('\n')
    print('O paciente ' + vName + ' POSSUI atendimento prioritario!')
    if vDoenca == 'SIM':
        print('O paciente ' + vName + ' deve ser direcionado para sala de espera reservada!')
    elif vDoenca == 'NAO':
        print('O paciente ' + vName + ' pode ser direcionado para sala de espera comum!')
    else:
        print('Informar a suspeita de doença infecto-Contagiosa')
else:
    print('\n')
    print('O paciente ' + vName + ' NÃO POSSUI atendiemnto prioritario!')
    if vDoenca == 'SIM':
        print('O paciente ' + vName + ' deve ser direcionado para sala de espera reservada!')
    elif vDoenca == 'NAO':
        print('O paciente ' + vName + ' pode ser direcionado para sala de espera comum!')
    else:
        print('Informar a suspeita de doença infecto-Contagiosa')
