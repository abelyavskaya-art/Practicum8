sentence = input().split(" ")
result = []

for word in sentence:
    if sentence.count(word) == 2 and word not in result:
        result.append(word)

print("".join(result))