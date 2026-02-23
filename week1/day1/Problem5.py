#week1/day1/Problem5.py
# Problem Statemet: Leap year checker

print("{:^30}".format("Welcome to the Leap Year Checker!"))
print("{:^30}".format("Please enter a leap year it should be 4 digit number"))
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")