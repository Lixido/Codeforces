n = int(input())
count = 0
for i in range(n):
    current_people, max_people = map(int, input().split())
    if max_people - current_people >= 2:
        count += 1
print(count)