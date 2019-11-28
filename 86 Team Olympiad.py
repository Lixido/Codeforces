n = int(input())
children = [int(i) for i in input().split()]
a = [i+1 for i in range(n) if children[i] == 1]
b = [i+1 for i in range(n) if children[i] == 2]
c = [i+1 for i in range(n) if children[i] == 3]
n_team = min(len(a), len(b), len(c))
print(n_team)
for i in range(n_team):
    print(a[i], b[i], c[i])