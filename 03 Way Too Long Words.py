num = int(input())
for i in range(num):
    word = input()
    length = len(word)
    print(word if length<11 else word[0]+str(length-2)+word[-1])