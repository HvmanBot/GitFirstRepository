## Operators
"""
Computers are incredible at doing math calculations. Now that we have learned about variables, let's use them with arithmetic operators to calculate things!

Python has the following arithmetic operators:

+ Addition
- Subtraction
* Multiplication
/ Division
% Modulo (returns the remainder)
** Exponentiation

score = 0           # score is 0
score = 4 + 3       # score is now 7
score = 4 - 3       # score is now 1
score = 4 * 3       # score is now 12
score = 4 / 3       # score is now 1.3333
score = 4 % 3       # score is now 1

print(score)        # Output: 1

And take a look at this code that calculates a 20% tip by calculating the total and then multiplying by a float (decimal number):

pizza = 2.99
coke = 0.99

total = pizza + coke

tip = total * 0.2

print(tip) # Output: 0.796

Another way to write this is using parentheses to calculate the total and the tip in one line of code:

tip = (pizza + coke) * 0.2

In Python, parentheses have the highest order of operations.
"""

# Now that we've learned about the basics of variables and operators, let's put them to use!
"""
Instructions
Create a temperature program that converts a temperature from Fahrenheit (°F) to Celsius (°C).

Google the current temperature of Brooklyn, NY (where Codédex is based) in °F.

Use the following formula and write it out in Python:

Celsius= (Fahrenheit - 32) / 1.8
Print out the converted temperature.
​"""
# Let's try it!

# Temperature Converterù
print("Here is your  temperature converter.")
# Start by creating a variable tF being the fahrenheit temperature given by an human Imput
tF = float(
    input("what is the °F Temperature you want to convert: ")
)  # float at the begining is to tell python the data type
# Formula to convert the user input to Celsius (°C)
celsius = float((tF - 32) / 1.8)
# Shows the Celsius Temperature
print("The Celcius temperature is:", celsius, "°C")

# or if I want to have only 2 values after the comma:
print(f"The Celcius temperature is: {celsius:.2f} °C")
# The "f" in "f-strings" stands for "formatted". F-strings are a feature introduced in Python 3.6 that allow for easy string formatting
# by embedding expressions inside string literals. By prefixing a string literal with "f" or "F", Python recognizes it as an f-string,
# enabling you to embed expressions directly within curly braces {}.

# Exponents
"""
Python can also perform exponentiation such as 2³ or 10².

In written math, we might see an exponent as a superscript number (like above), but typing superscripts isn't always easy on modern 
keyboards. Since exponentiation is super similar to multiplication, Python uses the notation **.

score = 2 ** 2      # score is 4
score = 2 ** 3      # score is now 8
score = 2 ** 4      # score is now 16
score = 2 ** 5      # score is now 32

print(score)        # Output: 32
"""
# BMI
"""
The body mass index (BMI) was created by a Belgian mathematician in the 1850s and it's used by health and nutrition professionals
to estimate human body fat in certain populations.

It is computed by taking an individual's weight (mass) in kilograms and dividing it by the square of their height in meters.
bmi = mass / height**2
Author's note: Psst. BMI is an archaic and oversimplified way to measure personal health. 
It was created by a mathematician — not a doctor! 💡
"""
# Create a bmi program that calculates your own BMI.

# bmi calculator

# mass is you weight in Kilograms
mass = float(input("(in kg) What is your weight?: "))
# h is your height in meters
h = float(input("(in meters) What is you height?: "))
# BMI calculator
bmi = mass / (h**2)
# print the BMI
print("your BMI is: ", bmi)
# or
print(f"your BMI is {bmi:.2f}")
