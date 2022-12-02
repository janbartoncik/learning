import re

my_list = '100,30 Kč',
            '10 000,00 Kč', 
            '10,000.00 Kč', 
            '10000 Kč', 
            '32.100,30 Kč', 
            '12,345,678.91 Kč',
            '100 Kč',
            '10 000 Kč', 
            '10,000 Kč', 
            '10000 Kč', 
            '32.100 Kč', 
            '12.345 Kč']

for i in my_list:
    ws = i.replace("Kč", '')
    x = re.sub(',','.', ws).replace(" ","")
   
    if len(x.split(".")) > 1:
        end = x.split(".")[-1]
        x = "".join([i for i in x.split(".")[:-1]]) + "." + end
    print(float(x))