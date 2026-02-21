import keyword

name = input()

if not (name[0].isalpha() or name[0] == '_'):
    print(f'{name} не может быть именем в языке Python')
    exit()

if keyword.iskeyword(name):
    print(f'{name} не может быть именем в языке Python')
    exit()

for letter in name:
    if not (letter.isalnum() or letter == '_'):
        print(f'{name} не может быть именем в языке Python')
        exit()

print(f'{name} может быть именем в языке Python')




