import time

print('Ola Mundo')
time.sleep(2.5)
print('TEMPO DE 2,5 SEG')

# Capturar o local agora
Agora = time.localtime()
print(type(Agora))
print(Agora)
print(time.strftime('%m/%d/%Y, %H:%M:%S', Agora ), '\n')

# Convertendo um string para time
vTimeText = '13 June, 2024'
vConvert = time.strptime(vTimeText, '%d %B, %Y')
print(f'{vConvert}')