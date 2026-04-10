MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0
coffee_machine = True

while coffee_machine :
    user_order = input("What would you like to order? ?(espresso, latte, cappuccino) :").lower()
    report = {
        'money': money,
        "water": resources["water"],
        "milk": resources["milk"],
        "coffee": resources["coffee"],
    }
    if user_order == "report":
        print(f"money: ${report['money']}\nwater : {report['water']}\ncoffee : {report['coffee']}\nmilk : {report['milk']}")

    else:
        if MENU[user_order]["ingredients"]["water"]> resources["water"] or MENU[user_order]["ingredients"]["milk"]> resources["milk"] or MENU[user_order]["ingredients"]["coffee"]> resources["coffee"]:
            print("Sorry, you cannot order! the resources is not enough!")

        else:
            user_qurters = int(input("Please insert coins.\nhow many quarters?: "))
            user_dimes = int(input("how many dimes?: "))
            user_nickles = int(input("how many nickles?: "))
            user_pennies = int(input("how many pennies?: "))
            total = user_qurters * .25 + user_dimes * .10 + user_nickles * .05 + user_pennies * 0.01
            if total < MENU[user_order]["cost"]:
                print("Sorry, you don't have enough money!")
            else :
                money += MENU[user_order]["cost"]
                total -= MENU[user_order]["cost"]
                print(f"Here is your change ${total} \nHere is your {user_order}")
                resources["water"] -= MENU[user_order]["ingredients"]["water"]
                resources["milk"] -= MENU[user_order]["ingredients"]["milk"]
                resources["coffee"] -= MENU[user_order]["ingredients"]["coffee"]
