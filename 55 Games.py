n = int(input())
colors = []
count = 0
for i in range(n):
    colors.append([int(t) for t in input().split()])
for i in range(n):
    for j in range(n):
        if colors[i][0] == colors[j][1]:
            count += 1
print(count)