#week1/day2/problem4.py
# Problem Statement: Palindrome checker
print("{:^30}".format("Welcome to the Palindrome Checker!"))
print("Please enter a string to check if it is a palindrome.")
input_string = input()
if len(input_string) == 0:
    print("You entered an empty string. Please enter a valid string.")
else:
    #remove spaces and convert to lowercase for accurate palindrome checking
    cleaned_string = input_string.replace(" ", "").lower()
    if (cleaned_string == cleaned_string[::-1]):
        print(f"The entered string '{input_string}' is a palindrome.")
    else:
        print(f"The entered string '{input_string}' is not a palindrome.")
    