# The comments in the cell below are there as a guide for thinking about the problem. However, if you feel a different way is best for you and your own thought process, please do what feels best for you by all means.
# Create a class called cart that retains items and has methods to add, remove, and show

from IPython.display import clear_output

class Cart():
    def __init__(self,space,items,wheels = 4):
        self.space = space
        self.items = items
        self.wheels = wheels
    
    """
        Cart will require 2 positional arguments:
        space: which expects to be an integer
        items: which is expected to be a list, which CAN be empty
    """

    def ShowShoppingCart(self):
        print("Here's what you've got so far:")
        print(self.items)
    
    def showSpace(self):
        print("Here's how much space you have left: ")
        space_left = self.space - len(self.items)
        if space_left < 3:
            print(f"Your cart's pretty full! You only have space for {space_left} more items...")
        else:
            print(f"You have space for {space_left} more items!")
    
    def addItem(self):
        purchase = input("What do you want to add? ")
        self.items.append(purchase.lower())

    def delItem(self):
        forsaken = input("What do you want to remove from the cart? ")
        self.items.remove(forsaken.lower())
        print(f"{forsaken.title()} has been removed from the cart.")
    
    def quitting(self):
        print(self.items)


def goShopping():
    stop_and_shop_cart = Cart(20,[])
    print("Welcome to Stop & Shop!")
    clear_output()
    while True:
        response = input("What would you like to do: add, remove, show, check space, or quit? ")
        if response.lower() == "add":
            stop_and_shop_cart.addItem()
        elif response.lower() == "remove":
            stop_and_shop_cart.delItem()
        elif response.lower() == "show":
            stop_and_shop_cart.ShowShoppingCart()
        elif response.lower() == "check space":
            stop_and_shop_cart.showSpace()
        elif response.lower() == "quit":
            print("Here's your cart! Have a wonderful day.")
            stop_and_shop_cart.quitting()
            break
        else:
            print("Sorry, try again!")

goShopping()