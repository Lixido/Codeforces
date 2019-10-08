n = int(input())
seq = list(map(int, input().split()))
result, sub = 1, 1
for i in range(n-1):
    if seq[i] <= seq[i+1]:
        sub += 1
    else:
        sub = 1
    result = max(result, sub)
print(result)