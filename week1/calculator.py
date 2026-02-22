#week1/day1/calculator.py
#Your first interactive calculator program!
print("Welcome to the interactive calculator!")
# Get user input for the first number
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform basic arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
print("The sum of", num1, "and", num2, "is:", addition)
print("The difference between", num1, "and", num2, "is:", subtraction)
print("The product of", num1, "and", num2, "is:", multiplication)
print("The type of num1 is:", type(addition))
print("Cast number addition to int of num2 is:", int(subtraction))

#Try it yourself: Run the program and enter different numbers to see the results of the calculations. You can also try adding more operations like division or modulus!
