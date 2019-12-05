import time

n = int(input())

start = time.time()
f = (n-1)+(n-2)

if n == 0 or n == 1:
    print(n)
else:
    print(f)

print("czas: ",  end = '')
print(start)
