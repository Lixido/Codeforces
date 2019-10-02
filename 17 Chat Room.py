word = input()
flag = 'YES'
for i in 'hello':
    if i in word:
        word = word[word.index(i)+1:]
    else:
        flag = 'NO'
        break
print(flag)

# Solution using regular expression
import re
if re.search("h.*e.*l.*l.*o", input()):
    print("YES")
else:
    print("NO")
