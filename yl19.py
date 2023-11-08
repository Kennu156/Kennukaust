a = input("Sisesta sõna või lause: ")
vowel = ['a', 'e', 'i', 'o', 'u','ü','õ','ä','ö']
count = 0
for letter in a:
    if letter in vowel:
        count += 1
print(count)