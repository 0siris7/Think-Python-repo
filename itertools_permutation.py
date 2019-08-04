# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
string = input()
a = string.split()
iters = int(a[1])

permutats = list(permutations(a, iters))

for i in permutats:
    print(i)
