import os
from art import logo

print(logo)

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
    "money": 0
}

i = 0
shut_down = False

def start():
    global shut_down
    user_request = input("What would you like? (espresso/latte/cappuccino): ")
    if user_request == 'report':
        report()
    elif user_request == 'off':
        shut_down = True
        os.system("cls")
    elif check_resources(user_request) == True and user_request != 'report':
        collect_money(user_request)
        
def report():
    print(resources["water"])
    print(resources["milk"])
    print(resources["coffee"])
    print(round(resources["money"], 3))

def check_resources(order):
    if order == "espresso" and MENU["espresso"]["ingredients"]["water"] <= resources["water"]  and MENU["espresso"]["ingredients"]["coffee"] <= resources["coffee"]:
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        return True
    elif MENU[order]["ingredients"]["water"] <= resources["water"] and MENU[order]["ingredients"]["milk"] <= resources["milk"] and MENU[order]["ingredients"]["coffee"] <= resources["coffee"]:
        resources["water"] -= MENU[order]["ingredients"]["water"]
        resources["milk"] -= MENU[order]["ingredients"]["milk"]
        resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
        return True
    else:
        print("Not enough resources :/")

def collect_money(user_request):
    quarters = float(input("How many quarters: "))
    dimes = float(input("How many dimes: "))
    nickles = float(input("How many nickles: "))
    pennies = float(input("How many pennies: "))
    verify_money(quarters, dimes, nickles, pennies, user_request)

def verify_money(quarters, dimes, nickles, pennies, user_request):
    total_money = (quarters*0.25) + (dimes*0.1) + (nickles*0.05) + (pennies*0.01)
    if total_money < MENU[user_request]["cost"]:
        print("Sorry that's not enough money. Money refunded")
    elif total_money > MENU[user_request]["cost"]:
        change = total_money - MENU[user_request]["cost"]
        print(f"Here is {round(change,3)} in change.\nEnjoy your {user_request}!")
    elif total_money == total_money - MENU[user_request]["cost"]:
        print("Order placed")
    resources["money"] += total_money
    
while not shut_down:
    start()