a = int(input('Sisesta positiive aastaarv: '))

if a % 4 and a % 400:
    print('Lihtaasta')
elif a % 100:
    print('Liigaasta')
else:
    print('lihtaasta')