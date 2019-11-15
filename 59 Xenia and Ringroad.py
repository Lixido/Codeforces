n, m = map(int, input().split())
houses = [int(i) for i in input().split()]
result = 0
for i in range(m-1):
    move = houses[i+1] - houses[i]
    if move >= 0:
        result += move
    else:
        result += n + move
result += houses[0] - 1
print(result)