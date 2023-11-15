import random

r = random.randrange(0, 101)

while True: 

    a = int(input('Sisesta number: '))

    if r == a:
        print('õige')
        break   

    elif r < a:
        print('väiksem')
    else:
        print('suurem')
