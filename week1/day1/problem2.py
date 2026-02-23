#week1/day1/Problem2.py
# Temperature Converter - Convert Celsius to Fahrenheit and Kelvin
print("Welcome to the Temperature Converter!")
print("This program converts Celsius to Fahrenheit and Kelvin.")
# Get user input for temperature in Celsius
print("Enter the temperature in Fahrenheit:")
fahrenheit = float(input());
#convert Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5.0/9.0
#convert Celsius to Kelvin
kelvin = celsius + 273.15
print(f"The Input temperature in Fahrenheit is: {fahrenheit}°F")
print("The Temperature in Celsius is: {:.2f}°C".format(celsius))
print("The Temperature in Kelvin is {:.2f}K".format(kelvin))

