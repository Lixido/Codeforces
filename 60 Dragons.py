strength, n = map(int, input().split())
data = []
for i in range(n):
    data.append([int(t) for t in input().split()])
data.sort(key = (lambda x: [x[0], -x[1]]))
# arrange the order according to threshold and reward(reverse)

flag = 1
for i in range(n):
    threshold, reward = data[i][0], data[i][1]
    if strength <= threshold:
        flag = 0
        print('NO')
        break
    else:
        strength += reward
if flag:
    print('YES')