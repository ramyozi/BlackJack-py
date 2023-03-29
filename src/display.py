import os

import os

def clear_display():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    print("===================================")
    print(" BLACKJACK ")
    print("===================================")

def display_game(player_hand, dealer_hand, bet_amount, show_dealer_card=False, winnings=0):
    clear_display()
    display_header()
    print()
    print(f"Bet: ${bet_amount}")
    print(f"Balance: ${player_hand.balance}")
    print()
    print("Dealer's hand:")
    dealer_hand.display(show_all=show_dealer_card)
    print()
    print("Your hand:")
    player_hand.display(show_all=True)
    if winnings > 0:
        print(f"You won ${winnings}!")
    print()

def display_results(result):
    print()
    print(result)
    print()

def display_menu():
    clear_display()
    display_header()
    print()
    print("1. Play Game")
    print("2. Quit")
    print()