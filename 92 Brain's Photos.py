r, c = map(int, input().split())
flag = 0
for i in range(r):
    colors = input().split()
    if flag:
        continue
    elif set(colors) - {'B', 'W', 'G'}:
        flag = 1
if flag:
    print('#Color')
else:
    print('#Black&White')