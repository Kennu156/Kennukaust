a = input('Sisesta string millel on vähemalt 7 sümbolit ja paarituarvuline: ')
a = a.strip()
print(a)
center = len(a) / 2


if  len(a) % 2 and len(a) > 7:
    print(a[center-1:center+2])
elif len(a) < 7:
    print('ei')
else:
    print(a)
