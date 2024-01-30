"""
A lot of the times inside conditions, we are comparing two values. To do so, we need to use a different type of operators called relational operators that compares values:

== equal to
!= not equal to
> greater than
< less than
>= greater than or equal to
<= less than or equal to


In chemistry, pH is a scale used to specify the acidity or basicity of a liquid.

Create a ph_levels program that checks whether a pH level is basic, acidic, or neutral.

First, create a ph variable and ask the user for a value between 0 and 14.
Write an if, elif, else statement that:
If ph is greater than 7, output "Basic".
If ph is less than 7, output "Acidic".
Else, output "Neutral".
"""
# let's try

# pH Level python verification
# asking for a pH float variable: in the range of 0 (acid) to 14 (basic) where 7 is (Neutral pH)
try:
    pH = float(input("Insert your solution's pH here: "))

    if pH == 7:
        print("Your Solution has a NEUTRAL pH")
    elif pH < 7:
        print("Your Solution's pH is ACID")
    elif pH > 7:
        print("Your Solution's pH is BASIC")
except ValueError:  # shows error if the input is not a float data type
    print("Invalid Format. Please insert a correct pH format")
