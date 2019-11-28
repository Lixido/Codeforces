n = int(input())
seats = []
flag = 0
for i in range(n):
    seats.append(input())
    if flag:
        continue
    elif 'OO' in seats[i]:
        seats[i] = seats[i].replace('OO', '++', 1)
        flag = 1
if flag:
    print('YES')
    for i in range(n):
        print(seats[i])
else:
    print('NO')