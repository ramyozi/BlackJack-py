from deck import Deck
from display import clear_display, display_header, display_game, display_results
from hand import Hand
from input_validation import validate_menu_input, validate_bet_input, validate_hit_stand_input


class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.balance = 1000
        self.bet_amount = 0

    def play_game(self):
        clear_display()
        display_header()
        self.bet_amount = validate_bet_input(self.balance)
        self.deal_cards()
        self.player_hand.display(True)
        display_game(self.player_hand, self.dealer_hand, self.bet_amount, True)
        while self.player_hand.get_value() <= 21:
            choice = validate_hit_stand_input()
            if choice == "h":
                self.hit()
                display_game(self.player_hand, self.dealer_hand, self.bet_amount)
            elif choice == "s":
                break
        if self.player_hand.get_value() > 21:
            self.lose_game()
        else:
            self.dealer_play()
            self.check_for_win()

    def deal_cards(self):
        self.player_hand.add_card(self.deck.draw_card())
        self.dealer_hand.add_card(self.deck.draw_card())
        self.player_hand.add_card(self.deck.draw_card())
        self.dealer_hand.add_card(self.deck.draw_card())

    def hit(self):
        self.player_hand.add_card(self.deck.draw_card())

    def dealer_play(self):
        while self.dealer_hand.get_value() < 17:
            self.dealer_hand.add_card(self.deck.draw_card())

    def check_for_win(self):
        player_value = self.player_hand.get_value()
        dealer_value = self.dealer_hand.get_value()
        if dealer_value > 21:
            self.win_game()
        elif player_value > dealer_value:
            self.win_game()
        elif player_value == dealer_value:
            self.tie_game()
        else:
            self.lose_game()

    def win_game(self):
        winnings = self.bet_amount * 2
        self.balance += winnings
        display_header()
        display_results("You win!")
        display_game(self.player_hand, self.dealer_hand, self.bet_amount, True, winnings)
        self.play_again()

    def tie_game(self):
        self.balance += self.bet_amount
        display_header()
        display_results("It's a tie!")
        display_game(self.player_hand, self.dealer_hand, self.bet_amount)
        self.play_again()

    def lose_game(self):
        display_header()
        display_results("You lose!")
        display_game(self.player_hand, self.dealer_hand, self.bet_amount, True)
        self.play_again()

    def play_again(self):
        choice = validate_menu_input("Do you want to play again? (y/n): ", ["y", "n"])
        if choice == "y":
            self.deck = Deck()
            self.player_hand = Hand()
            self.dealer_hand = Hand()
            self.play_game()
        else:
            print("Thanks for playing!")
if __name__ == "__main__":
    game = Blackjack()
    game.play_game()
