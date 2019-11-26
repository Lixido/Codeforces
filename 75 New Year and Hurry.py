n, time = map(int, input().split())
count = 0
for i in range(1, n+1):
    time += 5*i
    if time <= 240:
        count += 1
    else:
        break
print(count)