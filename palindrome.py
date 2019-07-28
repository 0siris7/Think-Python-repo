def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1 : -1]

s = input("> ")
c = last(s) + middle(s) + first(s)
print(f"{last(s)}\n{middle(s)}\n{first(s)}")
print(c)
