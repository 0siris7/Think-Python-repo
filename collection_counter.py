from collections import Counter

shoes = int(input())
sizes = [int(x) for x in input().split()]
size_tal = [i for i in Counter(sizes).items()]
#print(size_tal)

size_histogram = dict()
for i in size_tal:
    size_histogram[i[0]] = i[1]

#print(size_histogram)
customers = int(input())


that_day = [tuple(input().split()) for i in range(customers)]
tot = 0

#print(that_day)
for i in range(customers):
    if int(that_day[i][0]) in size_histogram:
        if size_histogram[int(that_day[i][0])] != 0:
            tot += int(that_day[i][1])
            size_histogram[int(that_day[i][0])] -= 1


print(tot)
