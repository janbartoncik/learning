#Funkce na formatování čísel
import re

#snažil jsem se se vymyslet asi všechny možnosti jak lze napsat celé číslo
my_list = ['10001', '10_002', '10.003,00', '10,004', '10,005,00', '10 0 06', '1we0. .007', '10.008,-']

for i in my_list:
    x = re.sub(',\d\d$','', i) #zde se odstraní ,00 z každého čísla v listu
    print(int(re.sub("[^0-9]",'', x))) #zde se odstraní všechny ostatní přebytečné znaky a zobrazí se výsledek