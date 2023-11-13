import random

options = ['kivi', 'paber', 'käärid']
r = random.choice(options)

while True: 
    a = input('Sisesta kivi, paber või käärid (Lõpetamiseks x): ')
    if a == 'x':
        break

    elif a == 'kivi' and r == 'käärid' or a == 'paber' and r == 'kivi' or a == 'käärid' and r == 'paber':
        print('Sinu võit!')
    elif a == 'kivi' and r == 'paber' or a == 'paber' and r == 'käärid' or a == 'käärid' and r == 'kivi':
        print('Sina kaotasid')
    else:
        print('Viik')

    




