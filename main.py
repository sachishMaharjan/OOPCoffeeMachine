from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        machine_on = False

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink_choice = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink_choice):
            is_payment_accepted = money_machine.make_payment(drink_choice.cost)
            if is_payment_accepted:
                coffee_maker.make_coffee(drink_choice)





