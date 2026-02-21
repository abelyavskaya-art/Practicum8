number = input("Введите четырёхзначное число: ")
count = 0

# Проверка числа.
if len(number) == 4 and number.isdigit():
    for num in number:
        if number.count(num) == 1:
            count += 1

    if count == len(number):

        for _ in range(25):
            print(" ")

        print("Игрок пытается отгадать число:")

        # Начало игры.
        for attempt in range(10):
            answer = input()

            if len(answer) != 4 or not answer.isdigit():
                print("Введите четырёхзначное число")
                continue

            ox = 0
            cow = 0

            for symbol in range(4):
                if answer[symbol] == number[symbol]:
                    ox += 1
                elif answer[symbol] in number:
                    cow += 1


            print(f'Быков: {ox} Коров: {cow}')

            if ox == 4:
                print("Победа!")
                break
            else:
                continue

        else:
            print("Проигрыш!")



