n = int(input())
names = {}
for i in range(n):
    new = input()
    if new not in names:
        names[new] = 0
        print('OK')
    else:
        names[new] += 1
        print(new+str(names[new]))