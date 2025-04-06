# short demo to see if the code works
import string

file = open('doc6.txt', 'r',)
read = file.readlines()
modified = []

for line in read:
    modified.append(line.strip())
print(modified)