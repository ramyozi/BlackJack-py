class Hand:
    def __init__(self):
        self.cards = []
        self.balance = 0

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        num_aces = 0
        for card in self.cards:
            if card.value.isdigit():
                value += int(card.value)
            elif card.value in ["Jack", "Queen", "King"]:
                value += 10
            else:
                num_aces += 1
                value += 11
        while num_aces > 0 and value > 21:
            value -= 10
            num_aces -= 1
        return value

    def display(self, show_all=False):
        if show_all:
            for card in self.cards:
                print(card)
        else:
            print("<<hidden>>")
            print(self.cards[1])


    def clear(self):
        self.cards = []
        self.balance = 0
