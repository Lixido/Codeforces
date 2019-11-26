input()
sit = [int(i) for i in input().split()]
crime, police = 0, 0
for i in range(len(sit)):
    if sit[i] == -1:
        if police == 0:
            crime += 1
        else:
            police -= 1
    else:
        police += sit[i]
print(crime)
