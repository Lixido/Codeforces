n, k = map(int, input().split())
no_odds = (n+1)//2
if k <= no_odds:
    print(2*k - 1)
else:
    print(2*(k - no_odds))