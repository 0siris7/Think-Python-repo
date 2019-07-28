fob = open('words.txt')
dicword = dict()
keys = fob.read()
keys = keys.strip()
keylist = keys.split('\n')
count = 0
for i in keylist:
    dicword[i] = count
    count += 1

print(dicword)
