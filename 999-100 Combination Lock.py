n = int(input())
orig = [int(i) for i in list(input())]
dest = [int(i) for i in list(input())]
move = lambda i: min(abs(orig[i]-dest[i]), 10-abs(orig[i]-dest[i]))
change = [move(i) for i in range(n)]
print(sum(change))