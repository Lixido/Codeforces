n = int(input())
words = ['hate' if i % 2 != 0 else 'love' for i in range(1, n+1)]
print('I '+' that I '.join(words)+' it')