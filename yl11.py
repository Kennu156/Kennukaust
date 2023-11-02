a = input('Sisesta string millel on vähemalt 7 sümbolit ja paarituarvuline: ')
a = a.strip()
print(a)

if len(a) < 7 and len(a) % 2:
    print('ei')
elif(len(a) > 7):
    print('ok')
else:
    print('ok')
