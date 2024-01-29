##Pattern
print("PATTERN")
# Line by Line
# Python is run one line at a time, from top to bottom.
# We can output multiple messages by using multiple print() functions

# Suppose we want the output to look exactly like this pattern below:
"""
       1
     2 3
   4 5 6
7 8 9 10
"""
# How can you do that?

# here is my solution for yall:

print("       1")
print("     2,3")
print("   4,5,6")
print("7,8,9,10")

# run and look for your self ;)

"""
then you ask ChatGPT to do the same and  it gives you this response:
rows = 4  # Define the number of rows in the pattern
number = 1  # Initialize the starting number

# Loop through each row
for i in range(1, rows + 1):
    # Print spaces for formatting
    print(" " * (rows - i), end="")
    
    # Loop through each number in the row
    for j in range(i):
        # Print the number and space
        print(number, end=" ")
        number += 1  # Increment the number for the next iteration
    
    # Move to the next line for the next row
    print()

But one day I will beat you ChatGPT!! xD
"""

## Initials
print("INITIALS")
"""    
First, start the program with a comment that says a fun fact about yourself.

Then, create your block letters with your initials.

For example, if your name is Dua Lipa, your initials would be D and L, and your block letters would look like this:


Fun fact about Dua Lipa

DDDD   L
D   D  L
D   D  L
D   D  L
D   D  L
D   D  L
DDDD   LLLLL

"""
# Let's try it!

print(
    "Fun fact: My name is Cristian Velasco from Bolivia but I speak better italian than my native language :s "
)
print("CCCCCC VV        VV")
print("CCCCCC  VV      VV")
print("CC       VV    VV")
print("CC        VV  VV")
print("CCCCCC     VVVV")
print("CCCCCC      VV")

## Snail Mail
"""
In this exercise, you will write a letter to your future self... in Python.

Take a moment and think about what you hope to achieve on this journey.

Use print() to output:

Today's date.
How you are feeling right now.
What you want to accomplish by learning to code.
A little message to your older, wiser, and programmer self.
Your favorite emoji to spice things up!
"""
# Let's  do it!

print("Date: 18.12.2023")
print("How I Feel Today?: Little Nervous")
print("What I want to accomplish coding?: Get a job, then be my own Boss")
print('Little sugestion from the future ME: "think BIG, Have Fun, Work Hard"')
print("xD,=D")

# So proud of me! i feel confident with the print() function. the sky is the only limit now
