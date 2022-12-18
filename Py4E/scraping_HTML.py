# The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file. 

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1642152.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# # Retrieve all spans
tags = soup('span')
lst = list()

for i in tags:
    x = re.findall('[0-9]+', str(i))
    for y in x:
        o = y.split()
        lst.append(o)
q = sum(lst, [])
print(sum([int(w) for w in q]))