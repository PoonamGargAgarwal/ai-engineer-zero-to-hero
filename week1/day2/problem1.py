# week1/day2/problem1.py
# Grade Calculator - Calculate letter grade based on percentage score
print({"{:^30}".format("Welcome to the Grade Calculator!")})
print("Please enter the percentage score (0-100):")
score = float(input())
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:    grade = 'F'
print(f"The percentage score {score} corresponds to the letter grade: {grade}") 