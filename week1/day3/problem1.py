#week1/day3/problem1.py
# Problem Statement: Create List of first 10 natural numbers and print the list
class NaturalNumbers:
    #initialize list of natural numbers up to n
    def __init__(self,n):
        self.n = n
        self.natural_numbers = []
    
    #print the list of natural numbers
    def print_list(self):
        i= 0
        for i in range(0, self.n,i+1):
            print(self.natural_numbers[i])
    
    #create a list of natural numbers up to n
    def create_list(self):
        if(self.n < 0):
            print("There is no list of natural numbers)")
        elif (self.n >= 0):
            i = 0
            self.natural_numbers = [0] * self.n
            for i in range(0,self.n, i+1): 
                print("Enter the next natural number")
                self.natural_numbers[i] = int(input())

    #mean of the list of natural numbers
    def mean(self):
        if self.n == 0:
            print("The list of natural numbers is empty. Cannot calculate mean.")
        else:
            total = 0
            i = 0
            for i in range(0,self.n, i+1):
                total += self.natural_numbers[i]
            total = sum(self.natural_numbers)
            mean_value = total / self.n
            print(f"The mean of the list of natural numbers is: {mean_value}")

    #median of the list of natural numbers
    def median(self):
        if self.n == 0:
            print("The list of natural numbers is empty. Cannot calculate median.")
        else:
            sorted_numbers = sorted(self.natural_numbers)
            mid = self.n // 2 #find the middle index for the sorted list
            if self.n % 2 == 0:
                median_value = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
            else:
                median_value = sorted_numbers[mid]
            print(f"The median of the list of natural numbers is: {median_value}")
    
    #mode of the list of natural numbers
    def mode(self):
        if self.n == 0:
            print("The list of natural numbers is empty. Cannot calculate mode.")
        else:
            frequency = {}
            for num in self.natural_numbers:
                if num in frequency:
                    frequency[num] += 1
                else:
                    frequency[num] = 1
            max_freq = max(frequency.values())
            modes = [num for num, freq in frequency.items() if freq == max_freq]
            print(f"The mode(s) of the list of natural numbers is/are: {modes}")

# main function to create and print the list of natural numbers and calculate the mean
print("Welcome to the List of Natural Numbers Generator!")
print("Please enter how many items you want in the list of natural numbers")
n = int(input())
if(n < 0):
    print("There is no list of natural numbers")
else:   
    shopping_item_list = NaturalNumbers(n)
    shopping_item_list.create_list()
    shopping_item_list.print_list()
    shopping_item_list.mean() 
    shopping_item_list.median()
    shopping_item_list.mode()