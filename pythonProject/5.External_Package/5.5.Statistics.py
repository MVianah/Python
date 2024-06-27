import random
import statistics

vList = []

for valor in range(0,11,1):
    vList.append(random.randint(0,10))

print(f'{vList}')

# Retirando a Media
vMedia = statistics.mean(vList)
print(f' Media -> {round(vMedia,2)}')

# Retirando a Mediana
vMediana = statistics.median(vList)
vList.sort()
print(f'{vList}')
print(f' Mediana ->  {vMediana}')

# Retirando a Moda
vModa = statistics.mode(vList)
print(f' Moda -> {vModa}')
