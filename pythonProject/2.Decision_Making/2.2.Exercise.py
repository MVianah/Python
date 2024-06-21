vNivelAcesso = input('Qual nivel de acesso do usuário: ').upper()

if vNivelAcesso == 'ADM' or vNivelAcesso == 'USR':
    vGenero = input('Qual o genero do usuario: ').upper()
    if vNivelAcesso == 'ADM':
        if vGenero == 'MASCULINO':
            print('Olá Administrador!')
        elif vGenero == 'FEMININO':
            print('Olá Adiministradora!')
        else:
            print('Genero não identificado, favor informar MASCULINO ou FEMININO.')
    else:
        if vGenero == 'MASCULINO':
            print('Olá Usuario!')
        elif vGenero == 'FEMININO':
            print('Olá Usuaria!')
        else:
            print('Genero não identificado, favor informar MASCULINO ou FEMININO.')
elif vNivelAcesso == 'GUEST':
        print('Olá visistante')
else:
    print('Olá Desconhecido!')