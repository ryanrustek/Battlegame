import random

pips = random.randint(1, 6)
print("You roll the die... it lands with", pips, "pips showing.")


prizes = ["a car", "$10000", "a pony", "$500000"]
prize_won = random.choice(prizes)
print("you turn the wheel of fortune... it lands on a prize of", prize_won + "!!")


cards = [1, 2, 3, 4, 5, 6, 7, 9, 9, 10, 11]
random.shuffle(cards)
print("the cards are now in this order: ")
print(cards)
