a, b = map(int, input().split())
diff = min(a, b)
same = (max(a, b) - diff) // 2
print(diff, same) 