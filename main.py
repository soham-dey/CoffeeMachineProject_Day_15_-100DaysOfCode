machine_stop = "No"
resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

user_coffee_choice = input("What would you like? espresso/latte/cappuccino: ")
profit = 0


def machine(coffee_choice):
    global resources
    global machine_stop
    global profit
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

    def quantity_check(choice, list_content):
        water_quantity = MENU[choice]["ingredients"]["water"]
        milk_quantity = MENU[choice]["ingredients"]["milk"]
        coffee_quantity = MENU[choice]["ingredients"]["coffee"]
        if MENU[choice]["ingredients"]["water"] <= resources["water"] and MENU[choice]["ingredients"]["milk"] <= \
                resources["milk"] and MENU[choice]["ingredients"]["coffee"] <= resources["coffee"]:
            return "OK"
        else:
            if MENU[choice]["ingredients"]["water"] > resources["water"]:
                list_content.append("Water")
                if MENU[choice]["ingredients"]["milk"] > resources["milk"]:
                    list_content.append("Milk")
                if MENU[choice]["ingredients"]["coffee"] > resources["coffee"]:
                    list_content.append("Coffee")
                return "Not Ok"

    def cost_check(u_penny, u_nickel, u_dime, u_quarter, u_choice):
        penny = 0.01
        nickel = 0.05
        dime = 0.10
        quarter = 0.25
        total_money = ((penny * u_penny) + (nickel * u_nickel) + (dime * u_dime) + (quarter * u_quarter))
        for i in MENU:
            if MENU[u_choice] == MENU[i]:
                if total_money == MENU[i]["cost"]:
                    return "match"
                elif total_money > MENU[i]["cost"]:
                    return int(total_money - MENU[i]["cost"])
                elif total_money < MENU[i]["cost"]:
                    return "Sorry, the money is insufficient. You get a refund."

    list_1=[]

    if coffee_choice == "off":
        machine_stop = "Yes"
    else:
        while machine_stop == "No":
            for key in MENU:
                if coffee_choice == key:
                    is_quantity_ok = quantity_check(coffee_choice, list_1)
                    if is_quantity_ok == "OK":
                        num_penny = int(input("Enter the number of Pennies: "))
                        num_nickel = int(input("Enter the number of Nickels: "))
                        num_dime = int(input("Enter the number of Dimes: "))
                        num_quarter = int(input("Enter the number of Quarters: "))
                        now_profit = ((0.01 * num_penny) + (0.05 * num_nickel) + (0.1 * num_dime) + (0.25 * num_quarter))
                        user_money = cost_check(num_penny, num_nickel, num_dime, num_quarter, coffee_choice)
                        if user_money == "match":
                            print(f"Great! Here's your {coffee_choice}")
                            resources["water"] -= MENU[coffee_choice]["ingredients"]["water"]
                            resources["milk"] -= MENU[coffee_choice]["ingredients"]["milk"]
                            resources["coffee"] -= MENU[coffee_choice]["ingredients"]["coffee"]
                            profit += now_profit
                            user_coffee_choice_new = input("What would you like? espresso/latte/cappuccino: ")
                            machine(user_coffee_choice_new)
                        elif user_money == "Sorry, the money is insufficient. You get a refund.":
                            print(user_money)
                            user_coffee_choice_new = input("What would you like? espresso/latte/cappuccino: ")
                            machine(user_coffee_choice_new)
                        elif int(user_money) > 0:
                            print(f"Great! Here's your {coffee_choice} and your change is ${user_money}")
                            resources["water"] -= MENU[coffee_choice]["ingredients"]["water"]
                            resources["milk"] -= MENU[coffee_choice]["ingredients"]["milk"]
                            resources["coffee"] -= MENU[coffee_choice]["ingredients"]["coffee"]
                            profit += (now_profit-int(user_money))
                            user_coffee_choice_new = input("What would you like? espresso/latte/cappuccino: ")
                            machine(user_coffee_choice_new)
                    elif is_quantity_ok == "Not Ok":
                        machine_stop = "Yes"
                        print(f"These items are insufficient: {list_1}")

            if coffee_choice == 'report':
                print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}ml \n Money: {profit}\n")
                user_coffee_choice_new = input("What would you like? espresso/latte/cappuccino: ")
                machine(user_coffee_choice_new)
            elif coffee_choice == "off":
                machine_stop = "Yes"




machine(user_coffee_choice)




