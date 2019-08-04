from itertools import product

A = input()
A = A.split(' ')
A = [int(x) for x in A]

B = input()
B = B.split(' ')
B = [int(x) for x in B]
print(tuple(product(A, B)))
