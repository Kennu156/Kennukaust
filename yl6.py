num3 = int(input('Sisesta number:-'))
num2 = int(input('Sisesta number:-'))
num1 = int(input('Sisesta number:-'))

if(num1 > num2 and num1 > num3):
    print(num1, 'on suurem')
elif(num1 < num2 and num2 > num3):
    print(num2, 'on suurem')
else:
    print(num3, 'on suurem')