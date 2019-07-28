fin = open('words.txt')
for line in fin:
    if len(line) > 20 and ' ' not in line:
        print(line)
