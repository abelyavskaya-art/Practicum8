text = input("Введите текст: ").split()
width = int(input("Введите ширину колонки: "))

all_lines = []
current_line = []
current_length = 0

for word in text:
    word_length = len(word)

    # Проверка, помещается ли слово с пробелами
    if current_length + word_length + len(current_line) <= width:
        current_line.append(word)
        current_length += word_length
    else:
        if current_line:
            # Сохраняем текущую строку.
            all_lines.append(current_line)
        # Начало новой строки.
        current_line = [word]
        current_length = word_length

# Последняя строка.
if current_line:
    all_lines.append(current_line)

# Обрабатываем все строки, кроме последней.
for i in range(len(all_lines) - 1):
    # Список слов для текущей строки.
    line_words = all_lines[i]

    # Если в строке одно слово.
    if len(line_words) == 1:
        word = line_words[0]
        spaces = width - len(word)
        print(word + ' ' * spaces)
    else:
        # Считаем общее количесвто всех букв.
        letters_total = 0
        for word in line_words:
            letters_total += len(word)

        # Сколько пробелов нужно добавить
        spaces_total = width - letters_total

        # Количество промежутков между словами
        gaps = len(line_words) - 1

        # Количество пробелов между словами
        space_per_gap = spaces_total // gaps

        # Остаток пробелов (добавляем к первым промежуткам)
        extra = spaces_total % gaps

        # Строим строку
        result = line_words[0]
        for j in range(1, len(line_words)):
            if j <= extra:
                spaces = space_per_gap + 1
            else:
                spaces = space_per_gap

            result += ' ' * spaces + line_words[j]

        print(result)

# Последняя строка (выравнивание по левому краю)
if all_lines:
    last_line = ' '.join(all_lines[-1])
    spaces = width - len(last_line)
    print(last_line + ' ' * spaces)