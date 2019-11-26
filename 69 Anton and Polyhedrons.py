n = int(input())
ans = 0
for i in range(n):
    poly = input()
    if 'T' in poly:
        ans += 4
    elif 'C' in poly:
        ans += 6
    elif 'O' in poly:
        ans += 8
    elif 'D' in poly:
        ans += 12
    elif 'I' in poly:
        ans += 20
print(ans)