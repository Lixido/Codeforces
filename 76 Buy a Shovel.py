price, change = map(int, input().split())
i = 1
while i*price % 10 != 0 and i*price % 10 != change:
    i += 1
print(i)