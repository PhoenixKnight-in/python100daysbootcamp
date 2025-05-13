# TODO: 2. Check resources sufficient to make drink order
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
    "money": 0.0
}
def make_coffee():
    for k1,v1 in MENU[coffee]["ingredients"].items():
        for k2,v2 in resources.items():
            if k1 == k2:
                resources[k2] = v2-v1
                break
    print(f"Here is your {coffee}. Enjoy!")


money = {"penny":0.01,"dime":0.10,"nickel":0.05,"quarter":0.25}
# TODO: 1.Print report of all coffee machine resources
coffee = "on"
amt = 0.0
while coffee != "off":
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    r = False
    if coffee  == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources["milk"]}")
        print(f"Coffee: {resources["coffee"]}")
        print(f"Money: ${round(amt,2)}")
    elif coffee in MENU:
        for k1,v1 in resources.items():
            for k2,v2 in MENU[coffee]["ingredients"].items():
                if v1 < v2 and k1 == k2:
                    print(f"Sorry there is not enough {k1}.")
                    r = True
        if not r:
            print("_____Insert coins_____")
            q = float(input("Enter the quarters: "))
            d = float(input("Enter the dimes: "))
            n = float(input("Enter the nickles: "))
            p = float(input("Enter the pennies: "))
            amt = 0.25*q+0.1*d+0.05*n+0.01*p
            if amt == MENU[coffee]["cost"]:
                resources["money"] += MENU[coffee]["cost"]
                make_coffee()
            elif amt > MENU[coffee]["cost"]:
                resources["money"] += MENU[coffee]["cost"]
                change = amt-MENU[coffee]["cost"]
                make_coffee()
                print(f"Here is ${round(change,2)} dollars in change.")

            else:
                print(f"Sorry that's not enough money for {coffee} of ${MENU[coffee]['cost']}. Money refunded ${amt}.")



