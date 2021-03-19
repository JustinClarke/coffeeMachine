import os

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

def start():
    user_request = input("What would you like? (espresso/latte/cappuccino): ")
    if user_request == 'report':
        report()
    if user_request == 'off':
        os.system("cls")
    print(check_resources(user_request))
    collect_money(user_request)

def report():
    for item in resources:
        print(f"{item} = {resources.get(item)}")

def check_resources(order):
    if order == "espresso":
        if MENU["espresso"]["ingredients"]["water"] <= resources["water"]  and MENU["espresso"]["ingredients"]["coffee"] <= resources["coffee"]:
            return True
    elif MENU[order]["ingredients"]["water"] <= resources["water"] and MENU[order]["ingredients"]["milk"] <= resources["milk"] and MENU[order]["ingredients"]["coffee"] <= resources["coffee"]:
            return True

def collect_money(user_request):
    quarters = input("Enter number of quarters")
    dimes = input("Enter number of dimes")
    nickles = input("Enter number of nickles")
    pennies = input("Enter number of pennies")
    verify_money(quarters, dimes, nickles, pennies, user_request)

def verify_money(quarters, dimes, nickles, pennies, user_request):
    total_money = (quarters*0.25) + (dimes*0.1) + (nickles*0.05) + (pennies*0.01)
    if total_money < MENU[user_request]["cost"]:
        print("Sorry that's not enough money. Money refunded")
    elif total_money > MENU[user_request]["cost"]:
        change = total_money - MENU[user_request]["cost"]
        print(f"Order placed. Change returned {change}")
    elif total_money == total_money - MENU[user_request]["cost"]:
        print("Order placed")
    resources["money"] += total_money

start()