# from paws_and_cart_MAIN import stock_file
import time


class Cart:
    def __init__(self) -> None:
        self.cart = []

    # Prints out the users cart, with the item name, price and subtotal of cart.
    def get_cart(self, prompt):
        print(f"\n{prompt}")
        print("-" * 75)
        total_cost = 0
        total_items = 0
        for item in (self.cart):
            item_total = (item.price * item.quantity)
            total_cost += (item.price * item.quantity)
            total_items += item.quantity
            print(
                f"{item.quantity}x {item.name}  \t£{item_total}")
            print("-" * 75)
        print(f"Subtotal ({total_items} item(s)): £{total_cost}")
        print("-" * 75)
        print("\n\n")

    # Adding item from stock list to users shoppng cart
    def add_item(self, stock, index):
        if index >= 0 and (index) <= len(stock.stock_list):
            if stock.stock_list[index] not in self.cart and stock.stock_list[index].stock_level > 0:
                self.cart.append(stock.stock_list[index])
                self.cart[-1].quantity += 1
                self.cart[-1].stock_level -= 1
                print(f"\n1x {self.cart[-1].name} added to your cart!")
                time.sleep(1)

            elif stock.stock_list[index] in self.cart and stock.stock_list[index].stock_level > 0:
                for item in self.cart:
                    if stock.stock_list[index].name == item.name:
                        item.quantity += 1
                        item.stock_level -= 1
                        print(f"\n1x {item.name} added to your cart!")
                        time.sleep(1)

            else:
                print(
                    f"{stock.stock_list[index].name} is currently out of stock, please choose another item")
                time.sleep(1)

        else:
            print("Not a valid choice")

    # Removes item from the users cart
    def remove_item(self, stock, index):
        if index >= 0 and (index) <= len(stock.stock_list):
            if stock.stock_list[index] in self.cart:
                for item in self.cart:
                    if stock.stock_list[index].name == item.name and item.quantity > 0:
                        item.quantity -= 1
                        item.stock_level += 1
                        print(f"\n1x {item.name} removed from your cart!")
                        time.sleep(1)
                        if item.quantity == 0:
                            self.cart.remove(stock.stock_list[index])

            else:
                print(
                    "You cannot remove an item that is not already in your cart")

    def checkout(self):
        self.get_cart("Checkout: ")
        user_input = input("Are you sure you wish to checkout? (Y/N) ")
        if user_input.lower() == "y":
            print("Thanks and see you again soon!")
