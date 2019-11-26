input()
welfares = [int(i) for i in input().split()]
ans = (len(welfares)*max(welfares)-sum(welfares))
print(ans)