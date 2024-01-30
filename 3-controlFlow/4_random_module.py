# Random
"""
In Python, modules are .py files containing Python code that can be imported inside another Python program. The Python standard 
library contains well over 200 modules that we can use.

We can use the .randint() function from a module called random to generate a random number from a range.

But first, let's import this module so we can use its functions.

import random

Next, we'll create a variable to store the randomly generated value. Declare a variable called num, and assign it to the function call:

num = random.randint(1, 9)

This will generate a random number between 1 and 9 (inclusive of both).

Together, the code will look like:
"""

import random

num = random.randint(1, 9)

print(num)

"""

Try running this code! ☝️

The output should be different each time it runs: 2, 8, 5, 9, 2, 1, 3...
"""


"""
The Magic 8 Ball is a popular office toy and children's toy invented in the 1940s for fortune-telling and advice seeking. 🎱

It's an oversized 8 ball with some of the following answers:

Yes - definitely.
It is decidedly so.
Without a doubt.
Reply hazy, try again.
Ask again later.
Better not tell you now.
My sources say no.
Outlook not so good.
Very doubtful.
Create a magic8.py program that can respond to any Yes or No questions with a different answer each time it executes.

The output should have the following format:

Question:      [Question]
Magic 8 Ball:  [Answer]

For example:

Question:      Is Codédex better than Udemy yet?
Magic 8 Ball:  Better not tell you now.
"""
# Ok, Let's try!

# importing Random modules
import random

# creating an array of possible answers
array_of_answers = [
    "Yes - definitely.",
    "It is decidedly so.",
    "Without a doubt.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
]

# creating an array of possible yes no questions as example for the user
yes_no_questions = [
    "Is the sky blue?",
    "Do elephants fly?",
    "Is Python a programming language?",
    "Are you a robot?",
    "Does 2 + 2 equal 4?",
]

# starting the interaction with the users
print("ask me for yes or no question like the example below:")

# the "\n".join is used to hide the "[]" brackets and format the text inside the showed array
print("\n".join(yes_no_questions))

# asking the user to insert his yes or no question and storing it in a variable (question)
question = str(input("Insert here your question: "))
# specifying the string data type as input

# in order to have a break from the user question and the generation of the random answer
# set a min word leght to start an if statement to add a little of logic to the program

min_length = 3

# if the user imput has less than 3 words inside it will print an error message to the user
# if the user input is correct then the script will make a random choise from the answer array
# and print it to the user as answer to his question

if len(question) <= min_length:
    print("insert a correct question")
else:
    selected_answer = random.choice(array_of_answers)
    print(selected_answer)
