def locked(word1, word2):
    word3 = []
    for i, j in zip(word1,word2): #zip is used to take similar pairs of the word: (1,1) (2,2) and so on
        word3.append(i)
        word3.append(j)

    return(''.join(word3))

a = input("WOrd1:")
b = input("Word2:")

c = locked(a, b)

print(c)
