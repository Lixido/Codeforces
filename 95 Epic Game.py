a, b, n = map(int, input().split())
def gcd(x, y):
    for i in range(min(x, y), 0, -1):
        if x%i==0 and y%i==0:
            return i
count = 0
while n > 0:
    if count%2==0:
        n -= gcd(n, a)
    else:
        n -= gcd(n, b)
    count += 1
print(1-count%2)
