import math
def Q(D):
    C = 50
    H = 30

    return round(math.sqrt((2 * C * D) / H))


ds  = [int(x) for x in input().split(',')]
res = []

for d in ds:
    res.append(Q(d))

word = []
for i in res:
    word.append(str(i))

print(','.join(word).rstrip(","))