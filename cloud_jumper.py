destination = int(input()) #The destination
jumper = 0 #Keeps track of jump pattern [1,2,3,1,2,3.......]
x = 0 #point where the dude is

def jump(x, jumper): #Increment according to condition
    if jumper == 0: 
        x += 1
        jumper += 1

    elif jumper == 1:
        x+= 2
        jumper+= 1

    else:
        x += 3
        jumper = 0

    return x, jumper


while True:
    if x == destination: #Satisfied
        print("YES")
        break

    elif x < destination: #Didnt reach destination
        x, jumper = jump(x, jumper)

    elif x > destination: #Overshot destination
        print("NO")
        break