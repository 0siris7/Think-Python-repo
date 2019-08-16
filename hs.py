class Card():
    def __init__(self,name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack


    def display_card(self):
        print(f"{self.name}:\nHealth: {self.health}\nAttack: {self.attack}")


Zilliax = Card('Zilliax', 5, 3)
Tundra_Rhino = Card("Tundra Rhino", 6, 2)

deck = []
deck.append(Zilliax)
deck.append(Tundra_Rhino)

for card in deck:
    card.display_card()
