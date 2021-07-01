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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

# TODO: PUT IN WHILE LOOP
on = True
while on:
    # TODO: 0. Ask what would you like and list options
    option = input("What would you like? (espresso, latte, cappuccino): ")

    # TODO: 1. print report of coffee machine resources
    def in_machine(item):
        return resources[item]

    # TODO: 2. check if resources sufficient for order
    # TODO: 2.1 def to pull ingredients inside menu->coffee->ingredients-> water, coffee, milk


    def num_ingredients(coffee, item):
        return MENU[coffee]['ingredients'][item]


    def check_resources(coffee):
        for i in MENU[coffee]['ingredients']:
            if resources[i] < MENU[coffee]['ingredients'][i]:
                print(f"Sorry there is not enough {i}")
                return False
        return True
        # if coffee == 'espresso':
        #     if num_ingredients(coffee, 'water') > in_machine('water'):
        #         print("Sorry there is not enough water")
        #         return
        #     elif num_ingredients(coffee, 'coffee') > in_machine('coffee'):
        #         print("Sorry there is not enough Coffee")
        #         return
        # else:
        #     if num_ingredients(coffee, 'water') > in_machine('water'):
        #         print("Sorry there is not enough water")
        #         return
        #     elif num_ingredients(coffee, 'milk') > in_machine('milk'):
        #         print("Sorry there is not enough milk")
        #         return
        #     elif num_ingredients(coffee, 'coffee') > in_machine('coffee'):
        #         print("Sorry there is not enough Coffee")
        #         return
        #     else:
        #         return


    if option == 'report':
        print(f"Water: {in_machine('water')}ml\nMilk: {in_machine('milk')}ml\nCoffee: {in_machine('coffee')}g\nMoney:${money}")
    else:
        if check_resources(option):
            # TODO: 3. check if change sufficient for order
            # TODO:3.1 ask for 4 inputs, quaters, dimes, nickles, pennies
            quarters = (float(input("How many quarters?"))) * .25
            dimes = (float(input("How many dimes?"))) * .10
            nickles = (float(input("How many nickles?"))) * .050
            pennies = (float(input("How many pennies?"))) * .010
            total = round(quarters + dimes + nickles + pennies, 2)

            # TODO 3.2 create function to access cost of each item MENU -> Coffee -> cost


            def price(coffee):
                return MENU[coffee]['cost']


            # TODO 3.3 check if total sufficient

            if total > price(option):
                change = round(total - price(option), 2)
                print(f"Here is your: ${change}")
                print(f"Here is your {option} ☕ Enjoy!")
            #   TODO: 3.4 minus resources from machine
                for i in MENU[option]['ingredients']:
                    resources[i] = resources[i] - MENU[option]['ingredients'][i]
                money += MENU[option]['cost']
            else:
                print("Sorry not enough money, money refunded")




