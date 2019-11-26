n = int(input())
if n >= 0:
    ans = n
else:
    # get rid of "-" when doing //
    ans = -min((-n)//10, 10*((-n)//100)+(-n)%10)
print(ans)