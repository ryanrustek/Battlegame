import random

high_score = 0


def dice_game():

    global high_score
    print("Current High Score:", (high_score))

    while True:
        print("1) Roll Dice\n 2) Leave Game")
        choice = input("Enter your choice: ")

        if choice == ("2"):
            print("Goodbye!")
            break

        elif choice == ("1"):
            die1 = random.randint(1, 6)
            print("You roll a...", (die1))
            die2 = random.randint(1, 6)
            print("You roll a...", (die2))
            roll = die1 + die2
            print("\n You have rolled a total of:", (roll))

            if roll > high_score:
                high_score = roll
                print("\n New High Score!")
        print("\nCurrent High Score: ", (high_score))


dice_game()
