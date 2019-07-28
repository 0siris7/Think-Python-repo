def histogram(s):
    '''USED TO GENERATE A HISTOGRAM'''
    histo = {}
    for i in s:
        if i in histo:
            histo[i] += 1

        else:
            histo[i] = 1

    return histo


hist = histogram('parrot') #Function call

def choose_from_hist(hister):
    '''Creates a mapping between list of dict values and the dictionary itself'''
    x = [a for a in hister.values()]
    map = {}
    k = 0
    for i in hister:
        for j in range(0 + k, len(x)):
            if hister[i] == x[j]:
                map[(i, x[j])] = j
                k += 1
                break
    x = [a / len(x) for a in x]
    x.append('#')
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i] > x[j]
    #print(map)


choose_from_hist(hist)
