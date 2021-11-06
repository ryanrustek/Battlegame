from banking_pkg import account


def atm_menu(your_name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + your_name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")

your_name = input("Enter name to register: ")

pin = input("Enter PIN: ")

balance = 0

print(your_name + " has been registered with a starting balance balance of $ " + str(balance) + "\n")

print("          === Automated Teller Machine ===          ")
print("LOGIN")

while True:
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter pin: ")

    if name_to_validate == your_name and pin_to_validate == pin:
        print("Login Successful!")
        break
    else:
        print("Invalid credentials!")

while True:
    atm_menu(your_name)
    option = input("choose an option")
    if option == "1":
        account.show_balance(balance)

    elif option == "2":
        balance = account.deposit(balance)

    elif option == "3":
        balance = account.withdraw(balance)

    elif option == "4":
        account.logout(your_name)
        break
    else:
        print("Invalid. Please choose from available options.")
