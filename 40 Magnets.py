n = int(input())
count = 0
last = ''
for i in range(n):
    magnet = input()
    if magnet != last:
        count += 1
        last = magnet
print(count)
