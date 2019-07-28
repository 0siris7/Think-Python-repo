def merge_tools(string, k):
    partition = len(string) // k

    x = []
    for i in range(0, len(string), partition):
        print(i)
        x.append(string[i : i + partition])
        print(x)
    #print(x)


merge_tools('AABCAAADA', 3)
