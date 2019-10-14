from PIL import Image #Python Image Library
import random
end = 100
def showboard():
    #Shows the board
    img = Image.open("snl.png")
    img.show()


def play():
    '''DRIVEN'''
    p1_name = input('Enter player 1: ') #Enter details
    p2_name = input('Enter player 2: ')
    pp1 = 0 #Initial point of player1
    pp2 = 0 #Initial point of player2
    turn = 0 #For player 1 or 2 's turn
    while(1):
        #Infinite loop
        if turn % 2 == 0:
            #Player1 turn
            print(f"{p1_name} turn")
            #Ask for choice to continue
            ch = input("Wanna continue?(1/0): ")
            if ch == '1':
                print(f"{p1_name} scored {pp1}")
                print(f"{p2_name} scored {pp2}")
                print("Quitting")
                break

            dice = random.randint(1, 6) #emulatesa die
            print(f"Dice: {dice}") #shows
            pp1 += dice

            pp1 = check_ladder(pp1)

            pp1 = check_ladder(pp1)

            if pp1 > end: #Check if player goes beyond board
                pp1 = end 
            print(f"{p1_name} Score: {pp1}")

            if reached_end(pp1):
                print(f"{p1_name} won")
                break 

        else:
        #Player2 turn
            print(f"{p1_name} turn")
            #Ask for choice to continue
            ch = input("Wanna continue?(1/0): ")
            if ch == '1':
                print(f"{p1_name} scored {pp1}")
                print(f"{p2_name} scored {pp2}")
                print("Quitting")
                break

            dice = random.randint(1, 6) #emulatesa die
            print(f"Dice: {dice}") #shows
            pp2 += dice

            pp2 = check_ladder(pp2)

            pp2 = check_ladder(pp2)

            if pp2 > end: #Check if player goes beyond board
                pp2 = end 
            print(f"{p2_name} Score: {pp2}")

            if reached_end(pp2):
                print(f"{p2_name} won")
                break 

def check_ladder(points):
    if points == 8:
        print('Ladder')
        return 26

    elif points == 21:
        print('Ladder')
        return 82  
    elif points == 43:
        print('Ladder')
        return 77  

    elif points == 50:
        print('Ladder') 
        return 91
    elif points == 54:
        print('Ladder')
        return 93
    elif points == 62:
        print('Ladder') 
        return 96
    elif points == 66:
        print('Ladder') 
        return 87
    elif points == 80:
        print('Ladder')     
        return 100

    else:
        return points


def check_snake(points):
    if points == 44:
        print('Snake')
        return 22
    
    elif points == 46:
        print('Snakes')
        return 5

    elif points == 48:
        print('Snakes')
        return 9

    elif points == 52:
        print('Snakes')
        return 11

    elif points == 55:
        print('Snakes')
        return 7
    
    elif points == 59:
        print('Snakes')
        return 17

    elif points == 64:
        print('Snakes')
        return 36

    elif points == 69:
        print('Snakes')
        return 33

    elif points == 73:
        print('Snakes')
        return 1

    elif points == 83:
        print('Snakes')
        return 19

    elif points == 92:
        print('Snakes')
        return 51

    elif points == 95:
        print('Snakes')
        return 24

    elif points == 98:
        print('Snakes')
        return 28

    else:
        return points #No snakes

def reached_end(points):
    if points == end:
        return True

    else:
        return False

showboard()

play()