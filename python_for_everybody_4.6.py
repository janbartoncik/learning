def computepay(h, r):
    if h <= 40:
        return h * r
    elif h > 40:
        return (40 * r + (h - 40) * 1.5 * r)

h = float(input("Enter Hours:"))
r = float(input("Enter rate:"))
p = computepay(h, r)
print("Pay", p)