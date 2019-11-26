# 3k=6+3(k-2); 3k+1=4+3(k-1); 3k+2=8+3(k-2)
n = int(input())
k = n // 3
if n % 3 == 0:
    print(6, 3*(k-2))
elif n % 3 == 1:
    print(4, 3*(k-1))
else:
    print(8, 3*(k-2))