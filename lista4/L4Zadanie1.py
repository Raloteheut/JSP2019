lista = []
n = int(input("długość listy : "))
for i in range(0, n):
    a = int(input())
    lista.append(a)

x = 0
i = 1

while x < len(lista):
    i = i * lista[x]
    x += 1
    print(i)
    
lista = [2, 3, 5, 7, 11, 13]
x = 0
s = 0
while x < len(lista):
    s = s + lista[x]
    x += 1
    print(s)