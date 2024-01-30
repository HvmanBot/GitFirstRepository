"""
An if statement is used to test a condition for truth:

If the condition evaluates to True, code in the if part is executed.
If the condition evaluates to False, code is skipped.
if condition:
  # code inside

For example, if the grade variable is greater than 60:

if grade > 60:
  print("You passed!")

The code "inside" the if statement must be indented (preferably 2 spaces).

# Else
An else clause can be optionally added to an if statement.

If the condition evaluates to True, code in the if part is executed.
If the condition evaluates to False, code in the else part is executed.
if grade > 60:
  print("You passed.")
else:
  print("You failed.")

The code "inside" the else clause must also be indented.

Instructions
Holy moly, because the class's average was super low on the test, the teacher just added a curve for the test grades! 😭
"""
# Create a grades program that checks whether a grade is above or below 55.
"""
Start by creating a variable called grade and give it a value between 0-100.

Write a if/else statement for the following:

If grade is greater than or equal to 55, then print "You passed."
Else, print "You failed."
After you run the code, change grade's value and rerun it. Do this a few times to make sure it's working as intended.
"""
# Let's do it!
# this is the easiest way
grade1 = int(input("Enter your grade: "))
if grade1 >= 55:
    print("you Passed!!")
else:
    print("you Failed!!")


# the format below is for handling errors in user input e.g. the user input is a letter (string) instead of a number (float)
try:
    # Asking for grade input
    grade = float(input("What's the grade?: "))

    # Checking if the input grade is within valid range
    if 0 <= grade <= 55:
        print("Failed!")
    elif 56 <= grade <= 100:
        print("You Passed!")
    else:
        print("Grade out of range (0-100).")

except ValueError:
    # Handling invalid inputs, such as strings
    print("Invalid input. Please enter a numeric value.")

# Elif One or more elif statements (short for "else if") can be optionally added in between the if and else to provide additional
# condition(s) to check. Sometimes two is simply not enough.
