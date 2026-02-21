hint = input('Введите подсказку: ')
word = input('Введите слово: ')

# Скрываем ответ, вводим 25 пустых строк.
for _ in range(25):
    print(" ")

print("Игрок пытается отгадать слово")
print(hint)

#Скрываем загаданное слово
result = ["*"] * len(word)
print("".join(result))

for attempt in range(10):
    choice = input("Буква или слово (0 - буква, 1 - слово)?")

    if choice == "0":
        letter = input()

        for i in range(len(word)):
            if letter == word[i]:
                result[i] = (word[i])

        current_word = "".join(result)
        print(current_word)

        if current_word == word:
            print("Победа!")
            break

    elif choice == "1":
        answer = input()

        if answer == word:
            print("Победа!")
            break

        else:
            continue

else:
    print("Проигрыш!")