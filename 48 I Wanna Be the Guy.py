n = int(input())
x = list(map(int, input().split()))[1:]
y = list(map(int, input().split()))[1:]
if len(set(x)|set(y)) == n: 
    print('I become the guy.')
else:
    print('Oh, my keyboard!')