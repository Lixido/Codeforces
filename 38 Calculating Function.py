n = int(input())
# result = 0
# for i in range(n):
#     result += (-1)**(i+1) * (i+1)
# print(result)

# The result can be easily calculated.
result = (-1)**n * n // 2
# // is the last calculated operator
# -5 // 2 -> -3
print(result)