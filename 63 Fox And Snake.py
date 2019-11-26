row, col = map(int, input().split())
for i in range(row):
    if i % 2 == 0:
        print('#'*col)
    elif i % 4 == 1:
        print('.'*(col-1)+'#')
    else: 
        print('#'+'.'*(col-1))