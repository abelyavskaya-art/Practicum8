sentence = input().split(' ')
result = sorted(sentence, key = len)
print(' '.join(result))