word = input()
cond_upper = sum(map(str.isupper, word)) > len(word) / 2  # Use map function!
if cond_upper:
    print(word.upper())
else:
    print(word.lower())