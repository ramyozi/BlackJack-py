def validate_menu_input(prompt, choices):
    while True:
        choice = input(prompt).lower()
        if choice in choices:
            return choice
        print("Invalid input. Please try again.")


def validate_bet_input(balance):
    while True:
        try:
            bet_amount = int(input(f"Your balance is ${balance}. How much would you like to bet? "))
            if bet_amount > balance:
                print("You cannot bet more than your balance.")
            elif bet_amount <= 0:
                print("You must bet a positive amount.")
            else:
                return bet_amount
        except ValueError:
            print("Invalid input. Please enter a number.")


def validate_hit_stand_input():
    while True:
        choice = input("Do you want to hit or stand? (h/s): ").lower()
        if choice in ["h", "s"]:
            return choice
        print("Invalid input. Please try again.")

