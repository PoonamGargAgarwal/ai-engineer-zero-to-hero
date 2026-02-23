#week1/day1/problem3.py
# Simple BMI Calculator - Calculate Body Mass Index based on user input
print("Welcome to the BMI Calculator!")
print("This program calculates your Body Mass Index (BMI) based on your weight and height.")
print("How do you want to entery your weight? (kg or lbs)")
print("For Kg: Enter 1")
print("For lbs: Enter 2")
print("Enter your choice:")
choice = int(input())
if (choice == 1): 
    print("Enter your weight in kg:")
    weight = float(input())
elif (choice == 2):
    print("Enter your weight in lbs:")
    weight = float(input()) * 0.453592 # Convert lbs to kg
else:
    print("Invalid choice. Please enter 1 for kg or 2 for lbs.")
    exit()
print("Enter your height in meters:")
height = float(input())
# Calculate BMI
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")
# Interpret BMI result
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:    print("You are obese.")    