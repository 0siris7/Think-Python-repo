from hs import Card
from collections import defaultdict


class Deck():
    """docstring for Deck."""
    def __init__(self):
        self.deck = defaultdict(int)
        self.cards = [Card(input("Name:"), input("Health:"), input("Attack:"),
        input("Rarity:")) for i in range(4)]

        for card in self.cards:
            self.deck[card.name] += 1

    def display(self):
        print(self.deck)



Hunter1 = Deck()
Hunter1.display()
