n, x = map(int, input().split())

if x > n**2:
    ans = 0
else:
    ans = 0
    for i in range(1, n+1):
        if x % i == 0 and x/i <= n:
            ans += 1
print(ans)

# multiples = [(i+1)*(j+1) for i in range(n) for j in range(n)]
# print(multiples.count(x))