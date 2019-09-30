n = int(input())
count = 0
for i in range(n):
    know = list(map(int, input().split()))
    if sum(know) >= 2: count += 1
print(count)
