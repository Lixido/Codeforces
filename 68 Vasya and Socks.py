n, m = map(int, input().split())
count = 0
while n > 0:
    count += 1
    n -= 1
    if count % m == 0:
        n += 1
print(count)