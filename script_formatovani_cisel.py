import re
my_list = ['100,3 Kč', '10 000,1 Kč', '10,000.10 Kč', '10000 Kč', '32.100,30 Kč', '12,345,678.91 Kč','100 Kč','10 000 Kč', '10,000 Kč', '32.100 Kč', '12.345 Kč']

for a in my_list:
    x = a.replace("Kč", '')
    y = re.sub(',','.', x).replace(" ","")
    if y[-3] == '.':
        t = y.split(".")
        end = y.split(".")[-1]
        z = ''.join(t[:-1])
        f = re.sub('[^0-9]','', z)
        xyz = f + '.' + end
        print(float(xyz))
    elif y[-2] == '.':
        t = y.split(".")
        end = y.split(".")[-1]
        z = ''.join(t[:-1])
        f = re.sub('[^0-9]','', z)
        xyz = f + '.' + end
        print(float(xyz))
    else:
        print(float(re.sub("[^0-9]",'', y)))