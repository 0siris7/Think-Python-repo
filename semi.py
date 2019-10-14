start = 1
end = 27 // 2
a = []
for val in range(start, end + 1):
   if val > 1:
       for n in range(2, val):
           if (val % n) == 0:
               break
       else:
           a.append(val)

print(a)

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        for k in range(len(a)):
            for l in range(k + 1, len(a)):
                if (a[i] * a[j]) + a[k] * a[l] == 27:
                    print(a[i] * a[j], a[k] * a[l])
