fin = open('words.txt')


def bi_search(fin):
    a = [x.strip() for x in fin]
    a.sorted()
    b = input('Enter string:')
    if len(a) % 2 != 0:
        mid = len(a) // 2 + 1
    else:
        
