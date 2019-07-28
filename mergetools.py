def merge_tools(string, k):
    partition = len(string) // k

    x = []
    for i in range(0, len(string), partition):
        x.append(string[i : i + partition])

    print(x)
    y = []
    z = []
    for i in x:
        k = list(i)
        for j in k:
            if j not in y:
                y.append(j)

        z.append(''.join(y))
        del y[:]

    print(z)




merge_tools('AABCAAADA', 3)
