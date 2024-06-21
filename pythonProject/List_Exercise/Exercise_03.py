# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

vName = input('Digite seu nome: ')
while len(vName) < 3:
    print('Nome invalido informe um nome que contenha mais de 3 caracteres')

    vName = input('Digite seu nome: ')

vIdade = int(input('Digite sua idade: '))
while vIdade <= 0 or vIdade > 150:
    print('Idade invalida informe uma idade entre 0 e 150')

    vIdade = int(input('Digite sua idade: '))

vSalario = float(input('Digite seu salario: '))
while vSalario <= 0:
    print('Salario invalido informe um salario maior que 0')

    vSalario = float(input('Digite seu salario: '))

vSexo = input('Digite seu sexo: ').upper()
while vSexo != 'F' and vSexo != 'M':
    print('Sexo invalido favor informar: ')
    print('F - Feminino')
    print('M - Masculino')

    vSexo = input('Digite seu sexo: ').upper()

vEstadoCivil = input('Digite seu estado civil: ').upper()
while vEstadoCivil != 'S' and vEstadoCivil != 'C' and vEstadoCivil != 'V' and vEstadoCivil != 'D':
    print('Estado civil invalido favor informar: ')
    print('S - Solteiro')
    print('C - Casado')
    print('V - Viuvo')
    print('V - Viuvo')
    print('D - Divorciado')

    vEstadoCivil = input('Digite seu Estado civil: ').upper()

print('Cadastro realizado com Sucesso')

