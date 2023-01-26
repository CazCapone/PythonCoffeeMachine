from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

isOn = True

cm = CoffeeMaker() 
mm = MoneyMachine()
menu = Menu()

while isOn:  
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")

    if choice.lower() == 'off':
        isOn = False

    elif choice.lower() == 'report':
        cm.report()
        mm.report()
    
    else:
        drink = menu.find_drink(choice)
        if cm.is_resource_sufficient(drink):
            print(f"That will be ${drink.cost:.2f}")
            if mm.make_payment(drink.cost):
                cm.make_coffee(drink)
