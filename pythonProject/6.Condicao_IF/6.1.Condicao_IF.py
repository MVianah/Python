import statistics

vNota1 = float(input('Digite a nota 1: '))
vNota2 = float(input('Digite a nota 2: '))

vMedia = statistics.mean([vNota1, vNota2])

if vMedia < 5:
    print(f'Aluno está em recuperação: {vMedia}')
elif vMedia >= 6 and vMedia <= 8:
    print(f'Aluno passou sem recuperação: {vMedia}')
else:
    print(f'Aluno excelente: {vMedia}')