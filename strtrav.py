def string_traversal(s):
    index = -1
    while abs(index) != len(s) + 1:
        print(s[index], end='')
        index = index - 1
    print("\n")

string_traversal('apple')
