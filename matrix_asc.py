R, C = [int(x) for x in input().split()]

max = []

for i in range(R):
    temp = []
    for j in range(C):
        temp.append(0)
    max.append(temp)

numb = 1

for i in range(R):
    for j in range(C):
        max[i][j] = numb
        numb += 1

for i in range(R):
    print(*max[i])
