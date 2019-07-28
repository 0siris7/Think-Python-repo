def palin(s):
    c = list(s)
    print(c)
    c.reverse()
    print(c)
    c = ''.join(c)
    print(c)
    if c == s:
        return True
    else:
        return False


s = input("> ")
print(palin(s))
