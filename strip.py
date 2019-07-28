import string

bad_char = string.whitespace + string.punctuation


def process(line, hist):
    line = line.replace('-', ' ')
    for i in line.split():
        i = i.strip(bad_char)
        i = i.lower()
        hist[i] = hist.get(i, 0) + 1


def histogram(book):
    fin = open(book)
    hist = {}
    for line in fin:
        process(line, hist)
    return hist


def search(hist, val):
    for i in hist:
        if val == i:
            print(i, hist[i])
            break


def most_common(hist):
    t = []
    for i, j in hist.items():
        t.append((j, i))

    t.sort(reverse = True)
    print(t[:10])

def difference(hist, hist2):
    '''k = {}
    for key in hist:
        if key not in hist2:
            k[key] = None'''

    return set(hist) - set(hist2)

hist = histogram('sherlock.txt')
hist2 = histogram('emma.txt')

print(f"HISTOGRAM1 : \n{hist}")
print("TOTAL WORDS:")
print(sum(hist.values()))

print(f"HISTOGRAM2 : \n{hist2}")
print("TOTAL WORDS:")
print(sum(hist.values()))


most_common(hist)

diff = difference(hist, hist2)
print(diff)
