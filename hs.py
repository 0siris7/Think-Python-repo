class Card():
    def __init__(self,name, health, attack, rarity):
        self.name = name
        self.health = health
        self.attack = attack
        self.rarity = rarity


    def display_card(self):
        print(f"Rarity: {self.rarity}\nName: {self.name}\nHealth: {self.health}\nAttack: {self.attack}")
