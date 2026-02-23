#week1/day1/problem4.py
# Problem Statement : Even Odd classification
print("Welcome to the Even Odd Classifier!")
print("Please enter an integer to check if it is even or odd.")
x = int(input())
if (x%2 == 0):
    print(f"The entered number {x} is even")
else:    print(f"The entered number {x} is odd")