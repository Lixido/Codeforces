n, k = map(int, input().split())
a = list(map(int, input().split()))
m = sorted(a, reverse=True)[k-1]
pick = [i for i in a if i >= m and i > 0]
print(len(pick))