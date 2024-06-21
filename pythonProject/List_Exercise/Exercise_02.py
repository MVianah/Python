# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

vName = input('Digite seu nome: ')
vSenha = input('Digite uma senha: ')

while vName == vSenha:
    print('A senha não pode ser a mesma que o nome do usuario favor digite outra senha.')
    vSenha = input('Digite uma senha: ')

if vName != vSenha:
    print('Usuario cadastrado com sucesso!!')

