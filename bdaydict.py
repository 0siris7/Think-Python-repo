from random import randint

def bday():
    t = []
    count = 0
    for i in range(23):
        t.append(randint(1,31))

    t.sort()

    for i in range(len(t) - 1):
        if t[i] == t[i + 1]:
            count += 1

    print(t, count)

bday()
