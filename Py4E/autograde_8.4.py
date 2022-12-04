# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method.
# The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.

import os
os.chdir('/Users/janbartoncik/Documents/GitHub/learning/Py4E')

fh = open('romeo.txt')
lst = list()
for line in fh:
    x = line.split()
    for y in x:
        piece = y.split()
        if piece not in lst:
            lst.append(piece)

lst.sort()
nlst = sum(lst, [])
print(nlst)