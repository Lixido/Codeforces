n = int(input())
columns = sorted(list(map(int, input().split())))
print(' '.join(str(i) for i in columns))