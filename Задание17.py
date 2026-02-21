expression = input("Введите арифметическое выражение: ")


# Функция для выполнения операции.
def operation(sign, num1, num2):
    if sign == '+':
        return num1 + num2
    elif sign == '-':
        return num1 - num2
    elif sign == '*':
        return num1 * num2
    elif sign == '/':
        if num1 % num2 == 0:
            return num1 // num2
        else:
            return num1 / num2


# Функция ля вычисления части выраженния
def operation_part(expr):

    numbers = []
    operations = []
    current_num = ''

    for i, num in enumerate(expr):
        # Отрицательные числа.
        if (num.isdigit() or (num == '-'
            and (i == 0 or expr[i - 1] in '+-*/('))):
            current_num += num
        else:
            # Положительные числа.
            if current_num:
                numbers.append(int(current_num))
                current_num = ''
            # Знак в выражении.
            if num in '+-*/':
                operations.append(num)

    # В строке остался символ, добавляем его в числа.
    if current_num:
        numbers.append(int(current_num))

    # Выполняем умножение и деление.
    i = 0
    while i < len(operations):
        if operations[i] in ('*', '/'):
            result = operation(operations[i],
                    numbers[i], numbers[i + 1])
            # Замена результата в списке чисел
            numbers[i] = result
            del numbers[i + 1]
            del operations[i]
        else:
            i += 1

    # Выполняем сложение и вычитание.
    result = numbers[0]
    for i in range(len(operations)):
        result = operation(operations[i], result, numbers[i + 1])

    return result


# Основной цикл обработки скобок.
while '(' in expression:
    # Находим самую внутреннюю пару скобок.
    start = -1
    end = -1

    for i in range(len(expression)):
        if expression[i] == '(':
            start = i
        elif expression[i] == ')':
            end = i
            break

    if start != -1 and end != -1:
        # Вычисляем выражение внутри скобок.
        inbac_expr = expression[start + 1:end]
        inbac_result = operation_part(inbac_expr)

        # Заменяем скобки на результат.
        expression = expression[:start] + str(inbac_result) + expression[end + 1:]

# Вычисляем итоговое выражение без скобок.
final_result = operation_part(expression)
print(f"Результат: {final_result}")
