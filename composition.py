def is_between(x, y, z):
    #print("FUNCT")
    if x <= y and y <= z:
        #print("IF")
        return True
    else:
        #print("ELSE")
        return False

x, y, z = map(int,input("Enter numbers:").split())
print(is_between(x, y, z))
