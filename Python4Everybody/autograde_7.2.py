# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
ltot = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    lf = line.find(":")
    lt = float(line[lf+1:])
    ltot = ltot + lt

print("Average spam confidence:",ltot/count)