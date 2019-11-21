import math
f = int(input("0 - stopnie na radiany \n1 - radiany na stopnie\n"))
if (f == 0):
    x = int(input('x = '))
    print(math.radians(x))
else:
    x = int(input('x = '))
    print(math.degrees(x))