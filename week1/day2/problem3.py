#week1/day2/problem3.py
# String reverse
print("Welcome to the String Reverser!")
print("Please enter a string to reverse:")
input_string = input()
if len(input_string) == 0:
    print("You entered an empty string. Please enter a valid string.")
else:
    reversed_string = ""
    for i in range(len(input_string),-1,-1):
        if (i-1) >= 0:
            reversed_string = reversed_string + input_string[i-1]
    print(f"The reversed string is: {reversed_string}")