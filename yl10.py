Name = input("Lisa enda nimi:")
print('Tervist', Name)

area = input('Sisesta oma elukoht:')
if 'Saaremaa' in area:
    print('Tere saarlane')

age = int(input('Sisesta enda vanus:'))
if age < 18:
    print('Olete liiga noore, et autot juhtida')
elif age == 18:
    print('Õnne täisealiseks saamise puhul')
elif age > 18:
    print('Võite autot juhtida')                     

