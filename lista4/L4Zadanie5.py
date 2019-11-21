import itertools
lista = []
n = int(input("długość listy : "))
for i in range(0, n):
    a = int(input())
    lista.append(a)
print(list(itertools.permutations(lista)))