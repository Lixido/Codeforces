n, m, a, b = map(int, input().split())
ans = min(b*(n//m) + a*(n%m), a*n, b*(n//m+1))
# don't forget the third condition
print(ans)