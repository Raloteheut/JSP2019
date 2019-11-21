import cmath

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

d = (b^2)-(4*a*c)

x1 = (-b-cmath.sqrt(d))/(2*a)
x2 = (-b+cmath.sqrt(d))/(2*a)

print(x1, x2)