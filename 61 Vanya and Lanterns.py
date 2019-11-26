n_lantern, length = map(int, input().split())
lanterns = sorted([int(i) for i in input().split()])
if len(lanterns) == 1:
    distance = [0]  # max(0) will err
else:
    distance = [lanterns[i+1] - lanterns[i] for i in range(len(lanterns)-1)]
result = max(lanterns[0], max(distance)/2, length-lanterns[-1])
print(result)