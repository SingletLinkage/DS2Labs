import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

if __name__ == "__main__":
    cards = []
    for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
        for rank in range(1, 14):
            cards.append(Card(suit, rank))

    TRIALS = 50000
    wins = 0
    total = 0

    for _ in range(TRIALS):
        cardA = random.choice(cards)
        cardB = random.choice(cards)

        if cardA.suit != cardB.suit:
            total += 1
            if cardA.rank == cardB.rank:
                wins += 1
    print(f'{wins=}  {total=}  Probability: {wins/total*100:.2f}%')
            