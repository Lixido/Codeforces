n_students, n_puzzles = map(int, input().split())
puzzles = sorted(list(map(int, input().split())))
least_diff = 9999
for i in range(n_puzzles-n_students+1):
    diff = puzzles[i+n_students-1] - puzzles[i]
    least_diff = min(least_diff, diff)
print(least_diff)