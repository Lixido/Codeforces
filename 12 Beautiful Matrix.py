for i in range(5):
    row = input()[::2]
    if '1' in row:
        hmove = abs(row.index('1') - 2)
        vmove = abs(i-2)
        # break
print(hmove + vmove)
