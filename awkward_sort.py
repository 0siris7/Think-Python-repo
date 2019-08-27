import random

n = int(input())
list_1 = []

for i in range(n):
    list_1.append(int(input()))

while True:
    i = random.randint(0, n - 1)
    j = random.randint(0, n - 1)
    list_1[i], list_1[j] = list_1[j], list_1[i]
    if list_1 == sorted(list_1):
        break

print(*list_1)
