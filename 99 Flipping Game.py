n = int(input())
nums = [int(i) for i in input().split()]
flip = [1-i for i in nums]
ans = 0
for i in range(n):
    for j in range(i, n):
        new = list(nums[0:i]) + list(flip[i:j+1]) + list(nums[j+1:])
        ans = max(ans, sum(new))
print(ans)