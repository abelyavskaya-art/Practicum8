text = input()
counter = 0
result = []

for symbol in text:
    if text.count(symbol) == 3 and symbol not in result:
        result.append(symbol)
        break

print("".join(result))

