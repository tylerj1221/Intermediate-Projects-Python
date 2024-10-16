from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

def coffee_machine():
    is_running = True
    print(logo)
    while is_running:
        options = menu.get_items()
        choice = input(f"What would you like?\n{options}\n").lower()
        if choice == "off":
            is_running = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if drink is None:
                coffee_machine()
            elif coffee_maker.is_resource_sufficient(drink):
                print(f"That will be ${drink.cost}")
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
                else:
                    coffee_machine()
            else:
                coffee_machine()


coffee_machine()