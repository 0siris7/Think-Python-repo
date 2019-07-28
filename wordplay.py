fin = open('words.txt')

'''for line in fin:
    if len(line) == 20:
        print(line)'''

#fin.seek(0)

def has_no_e(s):
    tot = len(s)
    count = 0
    for i in s:
        if 'e' not in i:
            count+= 1
            print(i)

    return count / tot * 100


a = [x.strip() for x in fin]

per = has_no_e(a)
print(per)
