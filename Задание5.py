row1 = input()
row2 = input()
row3 = input()
result = []

for letter in row1 + row2 + row3:
    if letter in row1 and letter not in row2 + row3:
        result.append(letter)
    elif letter in row2 and letter not in row3 + row1:
        result.append(letter)
    elif letter in row3 and letter not in row1 + row2:
        result.append(letter)

result = " ".join(result)
print(f'Буквы, использующиеся только в одной строке: {result}')


