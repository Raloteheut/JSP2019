import time

a = 0
b = 1
n = int(input())

start = time.time()
for i in range(n):
    c = a + b
    a = b
    b = c
    print(a)

print("czas: ",  end = '')
print(start)