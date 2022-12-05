# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

import os

os.chdir('/Users/janbartoncik/Documents/GitHub/learning/Py4E')

file = open('mbox-short.txt')
names = dict()
name = None
topoccure = None

for line in file:
    if line.startswith('From '):
        x = line.split()
        sender = x[1]
        names[sender] = names.get(sender, 0) + 1

name = None
topoccure = None
for k,v in names.items():
    if topoccure is None or v > topoccure:
        name = k
        topoccure = v
print(name, topoccure)