n, a, b, c = map(int, input().split())
count, ans = 0, 1
a, b, c = sorted([a, b, c])
for i in range(n//a, -1, -1):  # inverse order, so can break to save time
    for j in range((n-i*a)//b, -1, -1):
        if (n-a*i-b*j) % c == 0:
            count = i + j + (n-a*i-b*j)/c
            ans = max(count, ans)
            break
print(int(ans))