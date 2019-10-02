n = int(input())
capacity, people = 0, 0
for i in range(n):
    exit, enter = map(int, input().split())
    people = people - exit + enter  # people change, not capacity
    capacity = max(people, capacity)
print(capacity)
