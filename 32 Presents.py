n = int(input())
receive = list(map(int, input().split()))
give = []
for i in range(n):
    give.append(receive.index(i+1) + 1)
print(" ".join(str(i) for i in give))
# for i in give:
#     print(i, end=" ")  
# The problem is that the last element will also end with " ""