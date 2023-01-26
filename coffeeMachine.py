MENU = {
    "espresso" : {
        "ingredients" : {
            "water" : 50,
            "coffee" : 18,
        },
        "price" : 1.5,
    },
    "latte" : {
        "ingredients" : {
            "water" : 200,
            "milk" : 150,
            "coffee" : 24,
        },
        "price" : 2.5,
    },
    "cappuccino" : {
        "ingredients" : {
            "water" : 250,
            "milk" : 100,
            "coffee" : 24,
        },
        "price" : 3.0,
    }
}

Profit = 0

Resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,
}

def makeCoffee(drink):
    ingredients = MENU[drink]['ingredients']
    for i in ingredients:
        Resources[i] -= ingredients[i]
    global Profit
    Profit += MENU[drink]['price']

def checkResources(drink):
    isEnough = True
    ingredients = MENU[drink]['ingredients']
    for i in ingredients:
        if ingredients[i] > Resources[i]:
            print(f"Sorry, there is not enough {i}. Please make another selection.")
            isEnough = False
    return isEnough

def getCoins(total=0):
    total += int(input("How many quarters? ")) *.25
    total += int(input("How many dimes? ")) *.1
    total += int(input("How many nickles? ")) *.05
    total += int(input("How many pennies? ")) *.01
    print(f"You have inserted ${total:.2f}.")
    return total

def checkMoney(total, price):
    total = total
    if total == price:
        return True
    elif total > price:
        change = round(total - price, 2)
        print(f"Your change is ${change:.2f}.")
        return True
    else:
        more = price - total
        print(f"Please insert ${more:.2f}.")
        return False


## Main UI Section ##
isOn = True

while isOn:
    order = input("What would you like? ((E)spresso/(L)atte/(C)appuccino): ")

    if order.lower() == 'off':
        isOn = False
    
    elif order.lower() == 'report':
        print(f"Water: {Resources['water']}ml")
        print(f"Milk: {Resources['milk']}ml")
        print(f"Coffee: {Resources['coffee']}g")
        print(f"Money: ${Profit}")

    else:
        # To allow shorter product names
        if order.lower() == 'e' or order.lower() == 'espresso':
            drink = 'espresso'
        elif order.lower() == 'l' or order.lower() == 'latte':
            drink = 'latte'
        elif order.lower() == 'c' or order.lower() == 'cappuccino':
            drink = 'cappuccino'

        if checkResources(drink):
            price = MENU[drink]['price']
            print(f"Please insert ${price:.2f}.")
            total = getCoins()

            while not checkMoney(total, price):
                total += getCoins()
            else:
                makeCoffee(drink)
                print(f"Your {drink} is being brewed, Thank you!")
