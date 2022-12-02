import re
#výstup listu by měl být '100.30', '10000.0', '10000.0', '10000.0', '32100.30', '12345678.91', '100.0', '10000.0', '10000.0', '32100.0', '12345.0'
my_list = ['100,30 Kč', '10 000,00 Kč', '10,000.00 Kč', '10000 Kč', '32.100,30 Kč', '12,345,678.91 Kč','100 Kč','10 000 Kč', '10,000 Kč', '32.100 Kč', '12.345 Kč']

#Tahle loop funguje ale pouze pokud se nepřidají do listu formáty čísel bez teček a čárek
# for i in my_list:
    # ws = i.replace("Kč", '')
    # x = re.sub(',','.', ws).replace(" ","")
   
    # if len(x.split(".")) > 1:
    #     end = x.split(".")[-1]
    #     x = "".join([i for i in x.split(".")[:-1]]) + "." + end
    # print(float(x))

#Tahle loop mi vyhodí přesně ty části, které potřebuji a já chci, aby na konci mi to vyfluslo float číslo s decimals ve formátu XXXXXXX.XX jak je popsáno výše
for i in my_list:
    x = re.findall('(\d+)[,\.\s]', i)
    print(x)