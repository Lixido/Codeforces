input()
points = [int(i) for i in input().split()]
count, max_past, min_past = 0, points[0], points[0]
for i in range(1, len(points)):
    now = points[i]
    if max_past < now or min_past > now:
        count += 1
    max_past = max(max_past, now)
    min_past = min(min_past, now)
print(count)