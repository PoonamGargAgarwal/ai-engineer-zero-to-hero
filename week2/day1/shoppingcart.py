# Create shopping cart with list of items
import item

class Shoppingcart:
    # Initialize Item List
    def __init__(self,n):
        self.n = n
        self.itemlist = []
        

    #Add items to Shopping Cart
    def add_items_incart(self,qty,name,price):

        if len(self.itemlist) >= self.n:
            print("Shopping cart is full. Cannot add more items.")
        else:
            if self.isItemInCart(name):
                print(f"Item '{name}' already exists in the shopping cart. Cannot add duplicate items.")
            else:
                new_item = item.Item()
                if new_item.add_item(qty,price,name):
                    self.itemlist.append(new_item)


    #Print items in Shopping Cart
    def print_items(self):
        if len(self.itemlist) == 0:
            print("Shopping cart is empty.")
        else:
            for item in self.itemlist:
                item.print_item()
    
    #Calculate total price of items in Shopping Cart
    def calculate_total(self):
        total = 0
        for item in self.itemlist:
            total += item.price * item.qty
        return total
    
    def isItemInCart(self,name):
        for item in self.itemlist:
            if item.name == name:
                return True
        return False
    
    def remove_item(self,name):
        for item in self.itemlist:
            if item.name == name:
                self.itemlist.remove(item)
                return
        print(f"Item '{name}' not found in the shopping cart.")
    
    def clear_cart(self):
        self.itemlist.clear()
    
    def return_qty_itemname(self,name):
        count = 0
        for item in self.itemlist:
            if item.name == name:
                count += item.qty
        return count
    
if __name__ == "__main__":
    print("Welcome to the Shopping Cart!")
    print("Please enter the number of items you want to add to the shopping cart:")
    n = int(input())
    shopping_cart = Shoppingcart(n)
    while True:
        print("Enter item name (or 'done' to finish):")
        name = input()
        if name.lower() == 'done':
            break
        print("Enter item quantity:")
        try:
            qty = int(input())
        except ValueError:
            print("Error: quantity must be a number")
            continue
        try:
            print("Enter item price:")
            price = float(input())
        except ValueError:
            print("Error: price must be a number")
            continue
        shopping_cart.add_items_incart(qty,name,price)
    
    print("\nItems in the shopping cart:")
    shopping_cart.print_items()
    total_price = shopping_cart.calculate_total()
    print(f"\nTotal price of items in the shopping cart: {total_price}")
    