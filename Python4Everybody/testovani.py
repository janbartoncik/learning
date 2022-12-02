import re

y = '12,345,678.91 Kč'
x = y.split('.')
z = ''.join(x[:-1])
f = re.sub('[^0-9]','', z)
print(f)