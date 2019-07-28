def inverse(d):
    inverse = dict()
    for key in d:
        val = d[key]

        if val not in inverse:
            inverse[val] = [key]

        else:
            inverse[val].append(key)

        return inverse

word = input("ENTER WORD: ")

temp = dict()

for i in word:
    if i not in temp:
        temp[i] = 1

    else:
        temp[i] += 1

k = inverse(temp)
