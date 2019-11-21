def sum(n):
    if n < 2:
        return 1
    else:
        return 1 / n + (sum(n - 1))

n = int(input())
print(sum(n))