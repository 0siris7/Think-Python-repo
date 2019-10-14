from collections import defaultdict

occurence = defaultdict(list)
n, m = [int(x) for x in input().split()] #Get m and n

b = []
for i in range(n):
    occurence[input()].append(i + 1)

for i in range(m):
    b.append(input())

for i in b:
    if i in occurence:
        print(*occurence[i])

    else:
        print('-1')

