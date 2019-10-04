k, n, w = map(int, input().split())
result = max(0, w*(w+1)*k/2-n)
print(int(result))