text = input("Введите текст: ")

count = 0

for symbol in text:
    if symbol == '(':
        count += 1
    elif symbol == ')':
        count -= 1
        if count < 0:
            print("Неправильно")
            break
else:
    if count == 0:
        print("Правильно")
    else:
        print("Неправильно")
