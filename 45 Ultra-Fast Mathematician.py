a = list(input())
b = list(input())
c = ['0' if a[i]==b[i] else '1' for i in range(len(a))]
# c = [['0', '1'][a[i]==b[i]] for i in range(len(a))]
print(''.join(c))