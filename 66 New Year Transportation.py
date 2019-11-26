n, destination = map(int, input().split())
panels = [int(i) for i in input().split()]
loc = 1
while loc < destination:
    loc += panels[loc-1]
if loc == destination:
    print('YES')
else:
    print('NO')
