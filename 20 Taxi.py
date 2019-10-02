from math import ceil
input()
a, b, c, d = map(input().count, '1234')  # do not write 4 counts
result = d + c + ceil((max(0, a-c) + 2 * b) / 4)
# first consider d & c, then 1 can sit with 3, the rest 1 and 2 sit with 2
print(result)