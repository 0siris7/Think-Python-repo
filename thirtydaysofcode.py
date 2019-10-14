T = int(input())
strings = [list(input()) for _ in range(T)] #Get a list of list containing alphabets
print(strings)

for i in strings:
    temp1 = [] #stores even index xhar
    temp2 = [] #store odd index char
    for j in range(len(i)):
        if j % 2 == 0:
            temp1.append(i[j]) #append even
        
        else:
            temp2.append(i[j]) #append odd
    
    print(f"{''.join(temp1)} {''.join(temp2)}")
