word = input().lower()
# vowels = ['a', 'e', 'i', 'o', 'u', 'y']
vowels = 'aeiouy'
result = ''
for letter in word:
    if letter not in vowels:
        result = result + '.' + letter
print(result)

# print(''.join('.'+l for l in input().lower() if l not in 'aeiouy'))