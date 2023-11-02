import os

fail = input('Sisesta faili nimi: ')
split_tup = os.path.splitext(fail)
print(split_tup)

file_name = split_tup[0]
file_extension = split_tup[1]

print("File Extension: ", file_extension)