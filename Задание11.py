cities = input().split()
winner = ""

# Проверяем правила
for i in range(len(cities) - 1):
    # Сравниваем последнюю букву текущ. города с 1 буквой след.
    if cities[i][-1].lower() != cities[i + 1][0].lower():
        winner = "Петя" if (i + 1) % 2 == 0 else "Вася"
        break
else:
    if (len(cities) - 1) % 2 == 0:
        winner = "Петя"
    else:
        winner = "Вася"

print(winner)
