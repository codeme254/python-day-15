
MENU = {
    "espresso": {
        "ingredients":{
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "capuccino": {
        "ingredients":{
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    },
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
def check_sufficiency(coffee_type):
    if MENU[coffee_type]["ingredients"]["water"] > resources["water"]:
        print("sorry, there is not enough water")
        return False
    elif MENU[coffee_type]["ingredients"]["coffee"] > resources["coffee"]:
        print("sorry, there is not enough coffe")
        return False
    elif coffee_type != 'espresso' and MENU[coffee_type]["ingredients"]["milk"] > resources["milk"]:
        print("sorry, there is not enough milk")
        return False
    else:
        print("all resources are there")
        return True

def reduce_resources(coffee_type):
    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
    if coffee_type != 'espresso':
        resources["milk"]-= MENU[coffee_type]["ingredients"]["milk"]

making_process = True
while making_process:

    choice = input("what would you like? (espresso/latte/capuccino/ [report]): ").lower()

    if choice == 'latte' or choice == 'espresso' or choice == 'capuccino':
        if check_sufficiency(choice):
            quaters = float(input("How many quaters? "))*0.25
            dimes = float(input("How many dimes? "))*0.10
            nickels = float(input("How many nickels? "))*0.05
            pennies = float(input("How many pennies? "))*0.01
            total = quaters + dimes + nickels + pennies
            if total < MENU[choice]["cost"]:
                print(f"sorry, {total} is not enough money, money refunded")
                making_process = False
            else:
                reduce_resources(choice)
                change = total - MENU[choice]["cost"] 
                resources["money"] += total
                print(f"Here is your change of ${round(change, 2)}")
                print(f"Here is you {choice} enjoy.")
        else:
            print(f"We are very sorry, there are no enough resources to make {choice}")
            making_process = False
    elif choice == 'report':
        print("Water: " + str(resources["water"])+"ml")
        print("Milk: " + str(resources["milk"])+"ml")
        print("Coffee: " + str(resources["coffee"])+"g")
        print("Money: $" + str(round(resources["money"], 3)))
    elif choice == 'off':
        print("Coffe machine turned off")
        making_process = False
    else:
        print("invalid choice")
        making_process = False