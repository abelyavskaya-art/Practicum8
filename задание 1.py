text = input("Введите текст: ")

counter = 0
result = 0

for word in text:
    if word == " ":
        counter += 1
        if counter > result:
            result = counter
    else:
        counter = 0

print(result)