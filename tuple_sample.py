b = []
for i in range(6):
    a = input()
    b.append(tuple(a.split()))

print(b)


#or

b = [tuple(input().split()) for i in range(6)]
