size = input()

a = [int(numbs) for numbs in input().split()]
b = a[:]
b.reverse()
print(b)
c = []

for i, j in zip(a, b):
    c.append(i + j)
print(c)
