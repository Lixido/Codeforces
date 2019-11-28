n, m = map(int, input().split())
def change(n, m):
    if n == m:
        return 0
    elif n > m:
        return n-m
    else:
        if m % 2 == 0:
            return change(n, m//2)+1
        else:
            return change(n, m+1)+1
print(change(n, m))
