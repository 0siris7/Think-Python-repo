def nested_sum(t):
    tot = 0
    for i in t:
        for j in i:
            tot += j
    print(tot)


def cumsum(t):
    tot = 0
    s = []
    for i in range(len(t)):
        tot += t[i]
        s.append(tot)

    print(s)

def middle(t):
    print(t[1:-1])

def chop(t):
    del t[0]
    del t[-1]
    print(t)


def is_sorted(t):
    return t == sorted(t)

def has_duplicates(t):
    for i in range(len(t) - 1):
        if t[i] == t[i + 1]:
            print(True)


def is_anagram(l1, l2):
    return sorted(l1) == sorted(l2)




nested_sum([[1, 2], [3], [4,5,6]])
cumsum([1,2,3])
middle([1,2,3,4])
chop([1,2,3,4])
print(is_sorted([1,2,2]))
print(is_sorted(['b','a']))
has_duplicates([1,2,2,3])
print(is_anagram('larry', 'yarrl'))
