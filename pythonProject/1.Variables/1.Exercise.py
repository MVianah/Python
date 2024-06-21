## Declaro  para  o  senhor  Gonçalves  Dias  que  o  senhor  Humberto  Delgado
## esteve  presente  no  evento  SecurityCup  e  gastou  o  valor  de  R$  30,00  com  a
## entrada.

v_Responsavel = str(input('Digite o primeiro nome: '))
v_Funcionario = str(input('Digite o segundo nome: '))
v_Name_Evento = str(input('Digite o nome do evento: '))
v_Valor_Gasto = float(input('Digite o valor gasto no evento: '))

print('\n')
print('Declaro para o senhor ', v_Responsavel, 'que o senhor ', v_Funcionario, '\n',
      'esteve presente no evento ', v_Name_Evento, 'e gastou o valor de R$ ', str(v_Valor_Gasto), 'com a', '\n'
      'entrada.')
print('\n')
print('======================== Informação das variaveis =====================')
print('O tipo da variavel v_Name e: ', type(v_Responsavel))
print('O tipo da variavel v_Name2 e: ', type(v_Funcionario))
print('O tipo da variavel v_Name_Evento e: ', type(v_Name_Evento))
print('O tipo da variavel v_Valor_Gasto e: ', type(v_Valor_Gasto))
