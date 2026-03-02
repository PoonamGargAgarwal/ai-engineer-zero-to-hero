# Create Item Class with quantity as integer to hold item count, itemname and price in float to hold per price of item
class Item:
    # initialize item with price and qty
    def __init__(self):
        self.name=""
        self.price=0
        self.qty=0.00

    def add_item(self,qty,price,name):
        # Validate incoming parameters before setting them
        try:
            if name == "":
                print("Item name cannot be empty")
        except:
            print("Error validating item name")
            return False
        try:
            if price < 0:
                print("Price cannot be negative")
                return False
        except ValueError:
            print("Error: price must be a number")
            return False
        try:            
            if qty < 0:
                print("Quantity cannot be negative")
                return False
        except ValueError:
            print("Error: quantity must be a number")
            return False
        self.name = name
        self.price = price
        self.qty = qty
        return True
    
    def isValidItem(self):
        if self.isNameEmpty() or self.isPriceNegative() or self.isQtyNegative():
            print ("Cannot add item due to invalid input.")
            return False
        return True
    
    def isNameEmpty(self):
        if self.name == "":
            print("Item name cannot be empty")
            return True
        return False
    
    def isPriceNegative(self):
        if self.price < 0:
            print("Price cannot be negative")
            return True
        return self.price < 0
    
    def isQtyNegative(self):
        if self.qty < 0:
            print("Quantity cannot be negative")
            return True
        return self.qty < 0
    

    def print_item(self):
        print(f"Item Name: {self.name}")
        print(f"Quantity is: {self.qty}")
        print(f"Price is: {self.price}")

    

    


