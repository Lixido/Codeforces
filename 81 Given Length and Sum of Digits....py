n, s = map(int, input().split())
s_save = s

# don't forget all conditions
if s == 0 and n == 1:
    ansmax, ansmin = 0, 0
elif s == 0 and n > 1:
    ansmax, ansmin = -1, -1
elif s > n*9:
    ansmax, ansmin = -1, -1
else:
    ansmax, ansmin = 0, 0

    # max
    d, t = 0, 0
    for i in range(n):
        if s > 0:
            d = min(9, s)
        else:
            d = 0
        ansmax += d * (10**(n-1-i))
        s -= d

    # min
    s = s_save
    d, t = 0, 0
    if 1+9*(n-1) >= s:
        for i in range(n):
            if s-1 > 0:
                d = min(9, s-1)
            else: 
                d = 0
            ansmin += d * (10**i)
            s -= d
        ansmin += 10**(n-1)
    else:
        for i in range(n):
            d = min(9, s)
            ansmin += d * (10**i)
            s -= d

print(ansmin, ansmax)

    