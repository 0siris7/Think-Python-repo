numbers = list(input())
a = []
for i in numbers:
    if i not in a:
        a.append(i)

tot = [numbers.count(x) for x in a]
print(tot)
if 1 in tot:
    print("YES")

else:
    print("NO")
