v_Name = str(input('Digite seu nome: '))
v_Empresa = str(input('Qual sua empresa: '))
v_Qtde_Funcionario = int(input('Quantidade de funcionarios: '))
v_MediaMensalidade = float(input('Média salarial: '))

print('\n')
print('======================== Informações ======================')
print(v_Name + ',trabalha na empresa ' + v_Empresa)
print('Possui: '+  v_Qtde_Funcionario + 'funcionarios')
print('A média da mensalidade é de: ', str(v_MediaMensalidade))
print('\n')
print('====================== Validação do tipos de dados ========================')
print('O tipo de dado da variavel v_Name é: ', type(v_Name))
print('O tipo de dado da variavel v_Empresa é: ', type(v_Empresa))
print('O tipo de dado da variavel v_Qtde_Funcionario é: ', type(v_Qtde_Funcionario))
print('O tipo de dado da variavel v_MediaMensalidade é: ', type(v_MediaMensalidade))


