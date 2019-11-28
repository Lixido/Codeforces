b = int(input())
boys = sorted([int(i) for i in input().split()])
g = int(input())
girls = sorted([int(i) for i in input().split()])
count = 0
for i in range(len(boys)):
    boy = boys[i]
    for j in range(len(girls)):
        girl = girls[j]
        if boy - 1 <= girl <= boy + 1:
            count += 1
            girls = girls[j+1:]
            break
print(count)