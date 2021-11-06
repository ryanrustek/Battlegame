import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:

    card_choice = input("Press enter to pick a card \n q to Quit ")

    if card_choice.lower() == "q":
        break

    else:
        card = random.choice(diamonds)
        hand.append(card)
        diamonds.remove(card)
        print("Your hand: ", hand)
        print("Remaining cards in deck: ", diamonds)

    if not diamonds:
        print("There are no more cards to pick")
        break
