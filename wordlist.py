fin = open('words.txt')

def wordlist(fin):
    a = []
    a = [x.strip() for x in fin]

    return a


zeta = wordlist(fin)
print(zeta[:10])
fin.close()
