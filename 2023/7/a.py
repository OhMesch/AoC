from collections import Counter
from functools import total_ordering

high_card_map = {"A": "a",
                 "K": "b",
                 "Q": "c",
                 "J": "d",
                 "T": "e",
                 "9": "f",
                 "8": "g",
                 "7": "h",
                 "6": "i",
                 "5": "j",
                 "4": "k",
                 "3": "l",
                 "2": "m"}

@total_ordering
class Hand:
    def __init__(self, cards, bet):
        self.cards = cards
        self.bet = bet

        self.value = self.scoreHand()

    def scoreHand(self):
        count = Counter(self.cards)

        if len(count) == 1:
            hand_type = 0 #5 of kinda
        elif len(count) == 2:
            hand_type = 1 if 4 in count.values() else 2 #4 of a kind or full house
        elif len(count) == 3:
            hand_type = 3 if 3 in count.values() else 4 #3 of a kind or 2 pair
        elif len(count) == 4:
            hand_type = 5
        else:
            hand_type = 6

        high_card_list = "".join([high_card_map[card] for card in self.cards])

        return (hand_type, high_card_list)


    def __lt__(self, other):
        return self.value < other.value
    
    def __eq__(self, other):
        return self.value == other.value


def generateSolution(filename):
    all_hands = []
    for line in open(filename):
        cards, bet = line.strip().split()
        bet = int(bet)

        all_hands.append(Hand(cards, int(bet)))

    winnings = [h.bet*(len(all_hands) - i) for i,h in enumerate(sorted(all_hands))]

    return sum(winnings)
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))