n = int(input())
line = list(map(int, input().split()))
argmax, argmin = line.index(max(line))+1, line[::-1].index(min(line))+1
# argmin counts from the back
result = argmax + argmin - 2
if result + 2 <= n:
# if argmax + argmin <= n:
    print(result)
else:
    print(result-1)