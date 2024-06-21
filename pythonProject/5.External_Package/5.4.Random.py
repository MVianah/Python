import random

#gerador de numero randomico
vNumRandom = round(random.random() * 10)
print(vNumRandom)

# Pegar um numero random de dentro de uma lista
vList = []

for valor in range(0, 10, 1):
    vList.append(random.randint(0,100))
print(vList)

print(f'{random.choice(vList)}')


