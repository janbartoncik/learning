# The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find. 
# Start at http://py4e-data.dr-chuck.net/known_by_Torran.html

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

pos = int(input())-1
times = int(input())
url = input()

for idk in range(times):
    lst = list()
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    tags = soup('a')
    for tag in tags:
        o = tag.get('href', None)
        lst.append(o)
    print(lst[pos])
    url = lst[pos]