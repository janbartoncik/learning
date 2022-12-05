#In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

import re
import os
os.chdir('/Users/janbartoncik/Documents/GitHub/learning/Py4E')

file = open('regex_sum_1642150.txt')
lst = list()

for i in file:
    u = i.rstrip()
    x = re.findall('[0-9]+', u)
    for y in x:
        o = y.split()
        lst.append(o)
q = sum(lst, [])
print(sum([int(w) for w in q]))

# alternative way
# w = list(map(int, q))
# print(sum(w))