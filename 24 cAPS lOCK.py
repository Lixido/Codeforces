words = input()
# cond1 = words.isupper()
# cond2 = words.islower() and len(words)==1
# cond3 = words[0].islower() and words[1:].isupper()
# if cond1 or cond2 or cond3:
if words[1:].upper() == words[1:]:  # a sweeping generalization, even works for cond3
    words = words.swapcase()
print(words)