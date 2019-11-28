n = int(input())
for i in range(n):
    ang = 180 - int(input())
    if 360 % ang == 0:
        print('YES')
    else:
        print('NO')