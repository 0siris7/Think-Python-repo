import random
class Unit():
    def __init__(self, name, attack, health):
        self.name = name
        self.attack = attack
        self.health = health


class Fight:
    def __init__(self,unit1, unit2):
        self.unit1 = unit1
        self.unit2 = unit2

    def atk(self):
        while self.unit1.health >= 0 or self.unit2.health>= 0:
                    temp = random.choice([1,2])

                    if temp == 1:
                        print(f"{self.unit1.name.title()} : {self.unit1.health}\n{self.unit2.name.title()} : {self.unit2.health}")
                        self.unit1.health -= self.unit2.attack
                        print(f"{self.unit1.name.title()} attacked {self.unit2.name.title()} and dealt {self.unit1.attack}")
                    else:
                        self.unit2.health -= self.unit1.attack
                        print(f"{self.unit2.name.title()} attacked {self.unit1.name.title()} and dealt {self.unit2.attack}")


                    if self.unit1.health <= 0:
                        print(f"{self.unit1.name.title()} died")
                        break

                    elif self.unit2.health <= 0:
                        print(f"{self.unit2.name.title()} died")
                        break


tiny = Unit('tiny', 40, 100)
drow = Unit('Drow', 20, 300)

fight = Fight(tiny, drow)

fight.atk()
