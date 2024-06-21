import time
import random

# While
vLoop = 0

while vLoop <= 10:
    print(f'{vLoop}')
    vLoop += 1
    time.sleep(0.5)

# While - Utilizando IF
while True:

    vJogador1 = random.randint(0, 6)
    vJogador2 = random.randint(5, 10)

    if vJogador1 > vJogador2:
        print(f'Player1: {vJogador1} - Player2: {vJogador2}, FINALMENTE O PLAYER 1 VENCEU!!!!!!!!!')
        break
    else:
        print(f'Player1: {vJogador1} - Player2: {vJogador2}')
