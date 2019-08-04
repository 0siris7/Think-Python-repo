# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
string = input()
a = string.split()
iters = int(a[1])
stuff = list(a[0])
permutats = list(permutations(stuff, iters))
#print(permutats)
permutats.sort()
for items in permutats:
    print(''.join(items))
