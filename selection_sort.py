a = [int(x) for x in input().split()]
count = 0
for i in range(len(a)):
    min_index = i
    for j in range(i + 1, len(a)):
        if a[min_index] > a[j]:

            a.append(a[min_index])
            del a[min_index]
            count += 1



print(count)
