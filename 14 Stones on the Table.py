num = int(input())
arr = input()
count = 0
for cond in ['RR', 'GG', 'BB']:
    while cond in arr:
        count += 1
        index = arr.index(cond)
        arr = arr[:index] + arr[index+1:]
print(count)

# Alternative solution: 
num = int(input())
arr = input()
count = 0
color = stones[0]
for i in range(1,n):
    if stones[i] == color:
        count += 1
    else:
        color = stones[i]
print(count)