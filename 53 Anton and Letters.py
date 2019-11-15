line = input()[1:-1].replace(',', '')
letters = [i for i in line.split()]
print(len(set(letters)))