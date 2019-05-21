name=input('Jak masz na imię?\n')
if name=='Alicja':
    print('Cześć, Alicja')
else:
    age=int(input('Ile masz lat?\n'))
    if age<12:
        print('Nie jesteś Alicją dzieciaku')
    elif age>2000:
        print('W przeciwności do Ciebie Alicja nie jest nieśmiertelna')
    elif age>100:
        print('Nie jesteś Alicją dziadku')
