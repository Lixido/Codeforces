# dynamic programming
# list method
input()
seq = [int(i) for i in input().split()]
max_n = max(seq)
ans = [0] * (max_n + 1)
# count = {num:seq.count(num) for num in range(max(seq)+1)}
count = [0] * (max_n + 1)
for n in seq:
    count[n] += 1
ans[1] = count[1]
for i in range(2, max_n + 1):
    ans[i] = max(ans[i-2]+i*count[i], ans[i-1])
print(ans[-1])


# not useful
# recursion
def max_sum(n):
    if n == 0:
        return 0
    elif n == 1:
        return count[n]
    else:
        return max(max_sum(n-1), max_sum(n-2)+n*count[n])
# print(max_sum(max(seq)))

# iteration
i, beforelast, last = 2, 0, count[1]
while i <= max(seq):
    now = max(last, beforelast + i * count[i])
    beforelast, last = last, now
    i += 1
# print(now)

