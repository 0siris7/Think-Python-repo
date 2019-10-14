import random
doors = [0]*3
goatdoor = [0]*3
swap = 0
dont_swap = 0
x = random.randint(0, 2)
doors[x] = "BMW"
for i in range(0, 3):
    if i == x:
        continue

    else:
        doors[i] = 'Goat'
        goatdoor.append(i)

choice = int(input("ENter choice:"))
door_open = random.choice(goatdoor)
while door_open == choice:
    door_open = random.choice(goatdoor)

ch = input("SWAP?")
if ch == 'y':
    if doors[choice] == 'Goat':
        print("Player wins")
        swap += 1
    else:
        print("Lost")

elif doors[choice] == 'Goat':
    print("LOST")

else:
    print("WINS")
    dont_swap += 1

print(swap, dont_swap)
