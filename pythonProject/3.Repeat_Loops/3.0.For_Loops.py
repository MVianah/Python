# FOR - Utilizando contando externo

for i in range(0,11):
    print(f' Contador: {i}')
    i =+1


# FOR - Utilizando contado interno

for count in range(0,11,1):
    print(f' Contador: {count}')


# FOR - Utilizando Listas
vListaPaises = ['Brasil', 'Argentina', 'Uruguai', 'Chile', 'Paraguai', 'Bolivia', 'Equador',
                'Colombia', 'Suriname', 'Guiane', 'Goianai France']

for Loop in vListaPaises:
    print(f'{Loop}')

# FOR - Utilizando Lista e Dicionario

vList = ['Brasil', 'Argentina', 'Uruguai', 'Paraguai']

vDict = {
    'Brasil' : 'Real',
    'Argentina' : 'Peso ARG',
    'Uruguai' : 'Peso URU',
    'Paraguai' : 'Guarany'
}

for vPaises in vList:
    if vPaises == 'Brasil':
        print(f'Moeda do {vPaises} é {vDict[vPaises]}')
    else:
        pass

