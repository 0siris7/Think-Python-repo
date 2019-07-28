fin = open('words.txt')
for line in fin:
    if 'e' not in line:
        print(f"{line} : True")
