import math
N,V1,V2 = [int(x) for x in input().split()]

walk = (math.sqrt(2) * N) / V1
cab = 2*N / V2

if walk < cab:
    print('Walk')
else:
    print('Cab')
