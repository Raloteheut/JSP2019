
 a = int(input("a = "))
 b = int(input("b = "))
 c = int(input("c = "))


def obw():
    print("obwód: ", end='')
    print(a+b+c)


def pol():
      p = a + b + c
      print("pole: ", end='')
      print((p*(p-a)*(p-b)*(p-c)) ** 0.5)


def inf_b():
    if a == b == c:
        print("równoboczny")
    elif a==b or b==c or c==a:
        print("równoramienny")
    else:
        print("różnoboczny")


def inf_k():
    if a > b and a > c and (a ** 2) == ((b ** 2) + (c ** 2)) or b > a and b > c and (b ** 2) == ((a ** 2) + (c ** 2)) or c > b and c > a and (c ** 2) == ((a ** 2) + (b ** 2)):
        print("prostokątny")
    elif (a ** 2) > ((b ** 2) + (c ** 2)) or (b ** 2) > ((a ** 2) + (c ** 2)) or (c ** 2) > ((a ** 2) + (b ** 2)):
        print("rozwartokątny")
    elif (a ** 2) < ((b ** 2) + (c ** 2)) or (b ** 2) < ((a ** 2) + (c ** 2)) or (c ** 2) < ((a ** 2) + (b ** 2)):
        print("ostrokątny")
