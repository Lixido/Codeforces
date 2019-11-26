n = int(input())
queue = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
threshold = []
n_min, i = 1, 0
while n_min <= 10**9:
    threshold.append(n_min)
    n_min += 5 * 2 ** i
    i += 1
threshold.append(10**9+1)  # artificial max bound

# determine the ith round
r = 0
for i in range(len(threshold)):
    if threshold[i] < n < threshold[i+1]:
        r = i
        break

ind = ((n - threshold[r]) // (2**r)) % 5
print(queue[ind])

