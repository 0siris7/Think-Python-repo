import random

class Die():
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self, roll = 10):
        for i in range(roll):
            print(random.randint(1, self.sides + 1))



print('DIE1')
die1 = Die()
die1.roll_die()

print("DIE2")
die2 = Die(10)
die2.roll_die()

print("DIE3")
die3 = Die(20)
die2.roll_die()
