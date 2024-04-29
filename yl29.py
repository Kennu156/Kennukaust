import time
import random

name = input("Tere, mis sinu nimi on? ")
time.sleep(random.randrange(2, 5))	
print("Tervist " + name)

	
feeling = input("Kuidas läheb? ")
time.sleep(random.randrange(2, 5))

if 'hästi' in feeling.lower():
    print('Mul ka')
else:
    print('OK')

time.sleep(random.randrange(2, 5))

favcolour = input("Mis su lemmik värv on? ")
colours = ["punane","roheline","sinine","must","roosa","kollane","hall"]
time.sleep(random.randrange(2, 5))
print('Minu lemmik värv on ' + random.choice(colours))

age = int(input('Kui vana sa oled? '))
time.sleep(random.randrange(2, 5))

if age < 18:
    print('Sa oled alaealine')
else:
    print('Sa ei ole alaealine')

area = input('Kus sa sündinud oled?')
time.sleep(random.randrange(2, 5))

if 'saaremaal' in area.lower():
    print('Sa oled äge')
else:
    print('Sa oled veider')

time.sleep(random.randrange(2, 5))

question = input('Küsi minult midagi')
time.sleep(random.randrange(2, 5))
answer = ['Maj tea', 'ei oska öelda', 'Jään vastuse võlgu']
print(random.choice(answer))
