def caesar(s, num):
    new_s = ''
    k = 0
    for i in s:
        #print(i)
        k = ord(i)
        #print(k)
        k += num
        #print(k)
        if k > ord('z'):
            k -= 26
            #print(k)
            new_s += chr(k)
            #print(new_s)

        elif k < ord('a'):
            k += 26
            new_s += chr(k)
            #print(new_s)

        else:
            #print("ELSE")
            new_s += chr(k)


    #print(new_s)
    return new_s


a = input("Sting:")
b = int(input("Shift:"))
l = caesar(a,b)
print(l)
