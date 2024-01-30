# Logical Operators
"""
One more thing that we should learn is logical operators.

Logical operators, also known as Boolean operators, combine and evaluate two conditions. They are and, or, and not operators:

and returns True if both conditions are True, and returns False otherwise.
or returns True if at least one of the conditions is True, and False otherwise.
not returns True if the condition is False, and vice versa.
Here are some examples:

if hunger > 4 and anger > 1:
  print('Hangry')

If the hunger variable is greater than 4 and the anger variable is greater than 1, then the program prints "Hangry".

if coffee > 0 or bubble_tea > 0:
  print('☺️')

If the coffee variable is greater than 0 or the bubble_tea variable is greater than 0, then the program prints a smiley face.

if not tired:
  print('Time to code!')

If the tired variable is not True, then the program prints "Let's code!"

So you might be wondering: and and or are awfully similar, how do I remember the differences between the two? Let's break this down
in a table form:

  A	      B     A and B	  A or B
False	False	 False	   False
False	True	 False	   True
True	False	 False	   True
True	True	 True	   True

Instructions
Since 1927, "The Cyclone" rollercoaster has delighted riders visiting Coney Island in Brooklyn, New York. 🎢

They're now installing a new entry system (the height requirement is 137 cm and the cost is 10 credits) and need your help writing 
the program for it!

Create a Cyclone program.

Ask the user what their height is and how many credits they have, and store the values in a height variable and a credits variable.

Use a combination of relational and logical operators to create the rules:

If they are tall enough and have enough credits, print "Enjoy the ride!"
Else if they have enough credits, but they aren't tall enough, print "You are not tall enough to ride."
Else if they are tall enough, but they don't have enough credits, print "You don't have enough credits."
Else, print a message saying they have not met either requirement.
"""
try:
    # Take user input for height and credits, and convert them to float
    height = float(input("What's your height (cm)?: "))
    credits = float(input("How many credits do you have?: "))

    # If the user input is successfully converted to float, proceed with the following checks

    # Check conditions and print messages accordingly
    if height > 137 and credits > 10:
        print("Enjoy the ride!")
    elif height < 137 and credits > 10:
        print("Sorry, but you are not tall enough")
    elif height > 137 and credits < 10:
        print("Sorry, but you don't have enough credits")
    elif height < 137 and credits < 10:
        print("Sorry, but you don't have enough credits and you are not tall enough")
    else:
        # If none of the above conditions are met, print an error message
        print("There's some error in your input")
except ValueError:
    # If the conversion to float fails (e.g., if the user enters a non-numeric value),
    # handle the ValueError and print an error message
    print("Insert a correct numeric value")
