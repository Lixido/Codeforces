n = int(input())
coins = sorted(map(int, input().split()), reverse=True)
count, total, i = 0, 0, 0
while total <= sum(coins)/2:
    count += 1
    total += coins[i]
    i += 1
print(count)