sentence = input().split()
result = []

for word in sentence[1:]:
    if word == sentence[0]:
        continue
    else:
        current_word = True
        for letter in range(len(word)):
            if word.count(word[letter]) > 1:
                current_word = False
                break

        if current_word:
            result.append(word)

print(" ".join(result))

