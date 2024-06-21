import datetime

#Manipulando Data

vDate = datetime.datetime.now()
vFormat = vDate.strftime('%d/%m/%Y %H:%M:%S %A')
print('\n')
print(f'{vDate}')
print('\n')
print(f'{vFormat}')
print('\n')
print(type(vDate))

#Incluindo dias a data

vDateTime = datetime.datetime.now().date()
vFormat15 = vDateTime + datetime.timedelta(days=15)
print(f'{vFormat15.strftime('%d/%m/%Y')}')

