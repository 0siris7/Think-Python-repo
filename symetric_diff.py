n = input()
set1 = set([int(x) for x in input().split()])
m = input()
set2 = set([int(x) for x in input().split()])
sym_diff = set1.difference(set2)
sym_diff.update(set2.difference(set1))

for i in sorted(sym_diff):
    print(i)
