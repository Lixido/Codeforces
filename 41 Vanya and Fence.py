n, h = map(int, input().split())
friends = list(map(int, input().split()))
tall = [1 for height in friends if height > h]
print(n+len(tall))