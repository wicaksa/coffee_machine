resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

def askUser():
    """
    Asks for a user input and returns the answer.
    :return: String
    """
    return input("What would you like? (espresso/latte/cappuccino): ")

def checkResource(strDrink):
    """
    Checks if there are enough resources to make the drink.
    :param strDrink: String
    :return: Boolean
    """
    if strDrink == "espresso": # key
        return (MENU["espresso"]["ingredients"]["water"] <= resources["water"] and
                MENU["espresso"]["ingredients"]["coffee"] <= resources["coffee"])
    elif strDrink == "latte": # key
        return (MENU["latte"]["ingredients"]["water"] <= resources["water"] and
                MENU["latte"]["ingredients"]["milk"] <= resources["milk"] and
                MENU["latte"]["ingredients"]["coffee"] <= resources["coffee"])
    else: # cappuccino
        return (MENU["cappuccino"]["ingredients"]["water"] <= resources["water"] and
                MENU["cappuccino"]["ingredients"]["milk"] <= resources["milk"] and
                MENU["cappuccino"]["ingredients"]["coffee"] <= resources["coffee"])

def insertCoins():
    """
    Calculates the amount of money the user inputs. Returns the total the unser input.
    :return: float
    """
    #check quarters
    print("Please insert coins: ")
    quarters = int(input("Insert number of quarters: "))
    #check dimes
    dimes = int(input("Insert number of dimes: "))
    #check nickels
    nickels = int(input("Insert number of nickels: "))
    #check pennies
    pennies = int(input("Insert number of pennies: "))
    #calc total
    return (.25 * quarters) + (.10 * dimes) + (.05 * nickels) + (.01 * pennies)

def checkCoins(coins, drink):
    """
    Checks if the amount of coins is enough for the drink.
    :param coins: float
    :param drink String
    :return: Boolean
    """
    print (f'coins {coins} | cost: {MENU[drink].get("cost")}')
    return coins >= MENU[drink].get("cost")

def coffeeMachine(strInput):
    """
    Runs coffee machine depending on what the user inputs.
    :param strInput: String
    :return:
    """
    boolMachineOff = False

    if strInput == "off":
        print("Powering down...")
        boolMachineOff = True

    if (not boolMachineOff):
        if strInput == "report":
            for k, v in resources.items():
                print(f"{k}: {v}")
        else:
            if checkResource(strInput):
                # ask user to insert coins
                # calculate values of coins
                totalCoins = insertCoins()
                # check if user inserted enough money
                if not checkCoins(totalCoins, strInput):
                    # if not, refund money
                        print("Sorry not enough money. Money refunded.")
                else:
                        # check if they need change
                        # if totalCoins > price of drink, return change
                    if totalCoins > MENU[strInput].get("cost"):
                        change = totalCoins - MENU[strInput].get("cost")
                        print(f"Here's your change: {change}")
                    # make coffee
                    # deplete resources, add money
                    resources["water"] = resources.get("water") - MENU[strInput]["ingredients"].get("water")
                    if (strInput != "espresso"):
                        resources["milk"] = resources.get("milk") - MENU[strInput]["ingredients"].get("milk")
                    resources["coffee"] = resources.get("coffee") - MENU[strInput]["ingredients"].get("coffee")
                    resources["money"] = resources.get("money") + MENU[strInput].get("cost")
                    print(f'{resources.get("money")} + {MENU[strInput].get("cost")}')
                    print(f"Here's your {strInput}.")

# Main Loop
canOrder = True # start the loop
while canOrder:
    order = askUser()
    coffeeMachine(order)
