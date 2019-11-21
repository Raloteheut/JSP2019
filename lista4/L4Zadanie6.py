import colorsys

r = int(input("r = "))
g = int(input("g = "))
b = int(input("b = "))

hsv = colorsys.rgb_to_hsv(r, g, b)
print(hsv)
