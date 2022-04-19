#increment a value with leading zeroes in a number `x`


x = "01"

x = int(x)
x += 1
x = str(x).zfill(2)