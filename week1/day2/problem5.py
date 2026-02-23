#week1/day2/problem45.py
# Vowel Counter - Count the number of vowels in a given string
print("{:^30}".format("Welcome to the Vowel Counter!"))
print("Please enter a string to count the vowels:")
input_string = input()
if(len(input_string) == 0):
    print("You entered an empty string. Please enter a valid string.")
else:
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    print(f"The number of vowels in the entered string '{input_string}' is: {count}")