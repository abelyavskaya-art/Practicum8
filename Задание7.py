sentence = input().split()
min_word = len(sentence[0])

for word in sentence:
    if len(word) < min_word:
        min_word = len(word)

print(min_word)
