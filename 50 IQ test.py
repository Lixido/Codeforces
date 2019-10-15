n = int(input())
# numbers = list(map(int, input().split()))
# remainders = [i%2 for i in numbers]
remainders = [int(i)%2 for i in input().split()]
if sum(remainders) == 1:
    print(remainders.index(1)+1)
else:
    print(remainders.index(0)+1)