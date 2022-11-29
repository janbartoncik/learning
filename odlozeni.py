import re

my_list = ['100,30 Kč','10 000,00 Kč', '10,000.00 Kč', '10000 Kč', '32.100,30 Kč', '12.345,678.91 Kč']

for s in my_list:
    parts = list(re.findall('\d+', s))
    if len(parts) == 1 or len(parts[-1]) != 2:
        parts.append('0')
    print(float(''.join(parts[:-1]) + '.' + parts[-1]))