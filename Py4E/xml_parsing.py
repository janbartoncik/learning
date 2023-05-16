import urllib.request
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter location: ')
print('Recieving ', url)
xml_data = urllib.request.urlopen(url).read()

tree = ET.fromstring(xml_data)

# print('Retrieved', len(tree.read()), 'characters')

lst = tree.findall('comments/comment')
print('Count: ', len(lst))

sum = 0 

for element in lst:
    x = element.find('count').text
    sum = sum + int(x)

print('Sum: ', sum)