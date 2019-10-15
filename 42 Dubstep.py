# using re seems too complicated

# words = input().split('WUB')
# name = " ".join(words)

name = input().replace('WUB', ' ').strip()  # strip deletes space in the beginning and the end
name = ' '.join(name.split())  # multiple space -> space
print(name)