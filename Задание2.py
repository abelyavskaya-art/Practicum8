text = input("Введите текст: ")

# Используем 1, так как в строке точно есть один символ.
counter = 1
result = 1

"""Используем len(text) - 1, так как в последней итерации
 сравниваем предпоследний элемент с последним"""
for word in range(len(text) - 1):
    if text[word] == text[word+1]:
        counter += 1
        if counter > result:
            result = counter
    else:
        counter = 1

print(result)