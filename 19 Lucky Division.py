n = int(input())
lucky = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
flag = 'NO'
for i in lucky:
    if n % i == 0:
        flag = 'YES'
        break
print(flag)