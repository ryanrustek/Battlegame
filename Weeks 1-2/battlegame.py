wizard = "wizard"
elf = "elf"
human = "human"

wizard_hp = 70
elf_hp = 100
human_hp = 150
dragon_hp = 300

wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_damage = 50

print("1)   " + wizard)
print("2)   " + elf)
print("3)   " + human)
character = input("Choose your character: ")

while True:

    if character == "1" or character == "wizard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    if character == "2" or character == "elf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    if character == "3" or character == "human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("Unknown character")
        break

print("You have chosen the character: " + character)
print("health: " + str(my_hp))
print("damage: " + str(my_damage))

while True:
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragon's hitpoints are now: ", dragon_hp)

    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break

    my_hp = my_hp - dragon_damage
    print("The Dragon has damaged the", character)
    print("The", character + "'s", "hitpoints are now: ", my_hp)

    if my_hp <= 0:
        print("The", character, "has lost the battle.")
        break
