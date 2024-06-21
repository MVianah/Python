import random
import statistics

vListMedia = []

for valor in range(0,10,1):
    vListMedia.append(random.randint(0,100))

print(f'{vListMedia}')

# Retirando a Media
vMedia = statistics.mean(vListMedia)
print(f'{vMedia}')

# Retirando a Mediana
vMediana = statistics.median(vListMedia)
print(f'{vMediana}')

# Retirando a Moda
vModa = statistics.mode(vListMedia)
print(f'{vModa}')
