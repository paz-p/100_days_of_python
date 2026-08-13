from order_list import MENU, resources



def calulate_money():
    print("Please enter coins.")
    quarter = float(input("how many quarters?")) * 0.25
    dime = float(input("how many dimes?")) * 0.10
    nickel = float(input("how many nickels?")) * 0.05
    penny = float(input("how many pennies?")) * 0.01

    return quarter + dime + nickel + penny

def calulate_change(total,drink_cost):
    if total < drink_cost:
        print("You don't have enough money")
    else:
        change = total - drink_cost
        print(f"Your change is {change:.2f}")

def report(resources, profit):
    for item,amount in resources.items():
        if item == "coffee":
            print(f"{item.title()}: {amount}mg")
        else:
            print(f"{item.title()}: {amount}ml")
    print(f"Profit: ${profit}")

def check_ingredients(order,resources,MENU):
    ingredients = MENU[order]["ingredients"]
    for item,required_amount in ingredients.items():
        if resources[item] < required_amount:
            print(f"Sorry, there is not enough {item}")
            return False
        return True
def adjust_resources(order,resources,MENU):
    ingredients = MENU[order]["ingredients"]
    for item,amount in ingredients.items():
        resources[item] -= amount



more_orders = True
profit = 0
while more_orders:
    order = input("What would you like to order? (espresso/latte/cappuccino): ")

    if order == "report" :
        report(resources,profit)
    elif order == "off":
        print("Turning off....")
        more_orders = False
    else:
        if check_ingredients(order, resources, MENU):
            total = calulate_money()
            profit += total
            drink_cost = MENU[order]["cost"]
            if total >= drink_cost:
                calulate_change(total,drink_cost)
                adjust_resources(order, resources, MENU)
            else:
                print("Sorry, that's is not enough money")










