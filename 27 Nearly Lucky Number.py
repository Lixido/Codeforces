n = input()
count = n.count('4') + n.count('7')
if set(str(count)) <= set('47'):
    print('YES')
else:
    print('NO')