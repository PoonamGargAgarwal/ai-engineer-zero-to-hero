#Week1/day2/problem2.py
# Problem Statement: Simple Interest Calculator & Compound Interest Calculator
print ("{:^30}".format("Welcome to the Interest Calculator!"))
print("{:^30}".format("Please enter your choice:"))
print("{:^30}".format("1 for Simple Interest, 2 for Compound Interest, 3 for Exit"))
choice = int(input())
match choice:
    case 1: 
        print("Simple Interest Calculator")
        print("Please enter the principal amount:")
        principal = float(input())
        print("Please enter the annual interest rate (in %):")
        rate = float(input())
        print("Please enter the time period (in years):")
        time = float(input())
        simple_interest = (principal * rate * time) / 100
        print(f"The simple interest is: {simple_interest:.2f}")
    case 2: 
        print("Compound Interest Calculator")
        print("Please enter the principal amount:")
        principal = float(input())
        print("Please enter the annual interest rate (in %):")
        rate = float(input())
        print("Please enter the time period (in years):")
        time = float(input())
        print("Please enter the number of times interest is compounded per year:")
        n = int(input())
        compound_interest = principal * (1+(rate/100)/n)**(n*time) - principal
        print(f"The compound interest is: {compound_interest:.2f}")    
    case 3:
        print("Exiting the program. Goodbye!")
    case _:
        print("Invalid choice. Please enter 1 for Simple Interest, 2 for Compound Interest, or 3 to Exit.")