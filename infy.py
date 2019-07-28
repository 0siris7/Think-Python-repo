a = input('enter string: ')
k = dict()
z = [x for x in a.split(',')]
print(z)
for i in z:
    c, d = i.split(':')
    k[d] = c

count = 0

for i,j in k.items():
    for k in i:
        count += int(k) ** 2

    if count %  2 == 0:
        templist = list(j)
        for w in templist:
            if w == 'Z':
                templist[templist.index(w)] = 'A'
            elif w == 'z':
                templist[templist.index(w)] = 'a'
            else:
                temp = ord(w) + 1
                templist[templist.index(w)] = chr(temp)





    else:
        for w in templist:
            temp = ord(w) - 2
            if temp < ord('A') or temp < ord('a'):
                temp += 26
                templist[templist.index(w)] = chr(temp)



    count = 0




print(','.join(templist))
