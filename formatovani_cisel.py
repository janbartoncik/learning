#Funkce na formatování čísel
import re

my_list = ['10 0 0 0,00 Kč', '10,000.00 Kč', '10000 Kč', '32.100,30 Kč', '12,345,678.91 Kč']

for i in my_list:
    ws = i.replace("Kč", '')
    x = re.sub(',','.', ws).replace(" ","")
#    y = float(x)
#    print(re.sub("[^0-9]",'', x)) #zde se odstraní všechny ostatní přebytečné znaky a zobrazí se výsled#ek
    print(x)