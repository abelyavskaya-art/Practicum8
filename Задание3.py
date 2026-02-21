text = input().split(" ")
full_text = " ".join(text)
alphabet = []

for letter in full_text:
    if letter.isalpha() and letter not in alphabet:
        alphabet.append(letter)

print(alphabet)


